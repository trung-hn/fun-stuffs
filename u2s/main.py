# %%
from typing import Dict, List, Any, TypedDict, Iterable, Optional
from dataclasses import dataclass
from langgraph.graph import Graph, END, START
import json
from datetime import datetime
import logging
from typing_extensions import TypedDict
from enum import Enum
from prompts import ExtractionPrompt, FeedbackPrompt, TestEvaluationPrompt

# Setup logging with more detailed format
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Constants
MAX_ITERATIONS = 10
CONFIDENCE_THRESHOLD = 0.8
CRITICAL_ERROR_THRESHOLD = 0.3

"""
TODO
add support for schema validation (user-provided schema)

"""


@dataclass
class TestResult:
    name: str
    passed: bool
    confidence: float
    details: str
    partial_results: Optional[Dict[str, float]] = None


class WorkflowState(TypedDict):
    input_text: str
    extracted_json: Dict[str, Any]
    test_results: List[TestResult]
    evaluation: str
    feedback: str
    confidence_score: float
    iteration: int
    state_version: int


@dataclass
class StateVersion:
    version: int
    state: WorkflowState
    timestamp: datetime
    parent_version: Optional[int] = None


class StateManager:
    def __init__(self):
        self.states: Dict[int, StateVersion] = {}
        self.current_version = 0

    def save_state(self, state: WorkflowState) -> int:
        self.current_version += 1
        state_version = state.get("state_version", 0) + 1

        new_state = {**state, "state_version": state_version}

        self.states[self.current_version] = StateVersion(
            version=self.current_version,
            state=new_state,
            timestamp=datetime.now(),
            parent_version=self.current_version - 1,
        )
        return self.current_version

    def get_state(self, version: int) -> Optional[WorkflowState]:
        state_version = self.states.get(version)
        return state_version.state if state_version else None


class TestRunner:
    def __init__(self):
        self.test_history: Dict[str, List[TestResult]] = {}

    def run_test(
        self, test_case: Dict[str, Any], extracted_json: Dict[str, Any]
    ) -> TestResult:
        try:
            # Implement actual test logic here
            confidence = 0.9  # Example confidence score

            return TestResult(
                name=test_case["name"],
                passed=True,
                confidence=confidence,
                details="Test passed successfully",
                partial_results={"accuracy": 0.9, "completeness": 0.85},
            )
        except Exception as e:
            logger.error(f"Test failed: {str(e)}")
            return TestResult(
                name=test_case["name"],
                passed=False,
                confidence=0.0,
                details=f"Test failed: {str(e)}",
            )


def extraction_node(state: WorkflowState) -> WorkflowState:
    """Enhanced extraction node with error handling"""
    prompt = ExtractionPrompt().generate(
        input_text=state["input_text"],
        previous_feedback=state["feedback"] if state["iteration"] > 0 else "",
    )

    # In practice, send prompt to LLM here
    # extracted_data = llm(prompt)

    extracted_data = {
        "title": "Sample Title",
        "content": state["input_text"][:100],
        "metadata": {
            "date": datetime.now().isoformat(),
            "categories": ["auto-generated"],
        },
    }

    return {
        **state,
        "extracted_json": extracted_data,
        "confidence_score": 0.85,
    }


def test_runner_node(state: WorkflowState) -> WorkflowState:
    """Enhanced test runner with detailed results"""
    runner = TestRunner()
    test_cases = [
        {"name": "schema_validation", "level": "CRITICAL"},
        {"name": "data_quality", "level": "ERROR"},
        {"name": "completeness", "level": "WARNING"},
    ]

    results = []
    for test_case in test_cases:
        result = runner.run_test(test_case, state["extracted_json"])
        results.append(result)

        # Break early on critical failures
        if result.passed:
            break

    return {**state, "test_results": results}


def evaluation_node(state: WorkflowState) -> WorkflowState:
    """Enhanced evaluation node with detailed analysis"""
    prompt = TestEvaluationPrompt().generate(
        test_results=[t.__dict__ for t in state["test_results"]],
        extracted_json=state["extracted_json"],
    )

    failed_tests = [t for t in state["test_results"] if not t.passed]
    evaluation = ""
    if failed_tests:
        # In practice, send to LLM here
        # evaluation = llm(prompt)
        evaluation += f"Issues found: {', '.join(t.name for t in failed_tests)}"

    return {**state, "evaluation": evaluation}


def should_continue(state: WorkflowState) -> Iterable[str]:
    """Enhanced decision logic for workflow continuation"""

    # Check iteration limit
    if state["iteration"] >= MAX_ITERATIONS:
        return [END]

    # Check confidence threshold
    if state["confidence_score"] >= CONFIDENCE_THRESHOLD:
        return [END]

    # Continue if there are failed tests
    failed_tests = [t for t in state["test_results"] if not t.passed]
    if failed_tests:
        return ["feedback"]

    return [END]


def feedback_node(state: WorkflowState) -> WorkflowState:
    """Enhanced feedback node with history awareness"""
    prompt = FeedbackPrompt().generate(
        evaluation=state["evaluation"],
        test_results=[t.__dict__ for t in state["test_results"]],
        extracted_json=state["extracted_json"],
        iteration=state["iteration"],
    )

    # Generate targeted feedback based on test results
    failed_tests = [t for t in state["test_results"] if not t.passed]
    feedback_points = []
    for test in failed_tests:
        # In practice, send to LLM here
        # feedback = llm(prompt)
        feedback_points.append(f"Warning: {test.details}")

    feedback = "\n".join(feedback_points)

    return {**state, "feedback": feedback, "iteration": state["iteration"] + 1}


def create_extraction_workflow() -> Graph:
    """Create the enhanced workflow graph"""
    workflow = Graph()

    # Add nodes
    workflow.add_node("extract", extraction_node)
    workflow.add_node("test_runner", test_runner_node)
    workflow.add_node("evaluate", evaluation_node)
    workflow.add_node("feedback", feedback_node)

    # Define edges
    workflow.add_edge(START, "extract")
    workflow.add_edge("extract", "test_runner")
    workflow.add_edge("test_runner", "evaluate")
    workflow.add_edge("feedback", "extract")
    workflow.add_conditional_edges("evaluate", should_continue, ["feedback", END])

    return workflow.compile()


def run_extraction_pipeline(text: str) -> Dict[str, Any]:
    """Run the enhanced extraction pipeline"""
    state_manager = StateManager()

    initial_state: WorkflowState = {
        "input_text": text,
        "extracted_json": {},
        "test_results": [],
        "evaluation": "",
        "feedback": "",
        "confidence_score": 0.0,
        "iteration": 0,
        "state_version": 0,
    }

    # Save initial state
    state_manager.save_state(initial_state)

    workflow = create_extraction_workflow()
    workflow.get_graph().draw_mermaid_png(output_file_path="graph.png")
    final_state = workflow.invoke(initial_state)

    # Save final state
    state_manager.save_state(final_state)

    return {
        "json_data": final_state["extracted_json"],
        "status": (
            "success"
            if final_state["confidence_score"] > CONFIDENCE_THRESHOLD
            else "needs_review"
        ),
        "confidence_score": final_state["confidence_score"],
        "iterations": final_state["iteration"],
        "state_version": final_state["state_version"],
    }


if __name__ == "__main__":
    sample_text = "This is a sample text to extract information from."
    result = run_extraction_pipeline(sample_text)
    print(f"Extraction Result: {json.dumps(result, indent=2)}")

# %%
