import json

from dataclasses import dataclass
from typing import Dict, List

extraction_prompt_template = """# Information Extraction Task

## Context
You are a precise information extraction agent. Your task is to extract structured information from the given text according to the specified schema.

## Input Text
{input_text}

## Target Schema
{schema}

## Previous Feedback (if any)
{feedback_section}

## Instructions
1. Carefully read and analyze the input text
2. Extract information according to the schema requirements
3. Ensure all required fields are populated
4. Maintain data type consistency
5. Apply any feedback from previous iterations

## Output Format
Provide your response as a valid JSON object matching the target schema.

## Steps
1. First, identify key information in the text
2. Map identified information to schema fields
3. Validate data types
4. Fill in any missing required fields with appropriate default values
5. Format response as JSON

Please process the text and provide structured output:
"""

feedback_prompt_template = """# Extraction Feedback Generation Task

## Context
You are a feedback agent responsible for providing actionable suggestions to improve the extraction process. This is iteration {iteration}.

## Current Extraction
{extracted_json}

## Test Results
{test_results}

## Evaluation Summary
{evaluation}

## Instructions
1. Analyze the evaluation and test results
2. Identify specific areas for improvement
3. Provide concrete, actionable feedback
4. Consider iteration context

## Focus Areas
1. Failed test cases
2. Data quality issues
3. Missing or incorrect fields
4. Format inconsistencies
5. Schema violations

## Steps
1. Review evaluation findings
2. Identify key improvement areas
3. Formulate specific recommendations
4. Prioritize feedback points
5. Provide clear, actionable guidance

Please provide specific feedback for improvement:"""


evaluation_prompt_template = """# Test Results Evaluation Task

## Context
You are an evaluation agent responsible for analyzing test results and providing detailed assessment of the extraction quality.

## Extracted JSON
{extracted_json}

## Test Results
{test_results}

## Instructions
1. Analyze each test result in detail
2. Identify patterns in failures (if any)
3. Assess overall extraction quality
4. Determine if refinements are needed

## Evaluation Criteria
1. Schema compliance
2. Data quality
3. Completeness
4. Accuracy
5. Format consistency

## Steps
1. Review each test case result
2. Analyze failure patterns
3. Assess impact of failures
4. Determine if additional iterations needed
5. Summarize findings

Please provide your evaluation:"""


@dataclass
class PromptTemplate:
    """Base class for prompt templates with common formatting methods"""

    @staticmethod
    def format_dict(d: dict) -> str:
        return json.dumps(d, indent=2)

    @staticmethod
    def format_list(l: list) -> str:
        return "\n".join(f"- {item}" for item in l)


@dataclass
class ExtractionPrompt(PromptTemplate):
    def generate(self, input_text: str, previous_feedback: str = "") -> str:
        template = extraction_prompt_template
        feedback_section = (
            f"\nPrevious Iteration Feedback:\n{previous_feedback}"
            if previous_feedback
            else "None"
        )
        return template.format(
            input_text=input_text,
            schema="...",
            feedback_section=feedback_section,
        )


@dataclass
class TestEvaluationPrompt(PromptTemplate):
    def generate(self, test_results: List[Dict], extracted_json: Dict) -> str:
        return evaluation_prompt_template.format(
            extracted_json=self.format_dict(extracted_json),
            test_results=self.format_dict(test_results),
        )


@dataclass
class FeedbackPrompt(PromptTemplate):
    def generate(
        self,
        evaluation: str,
        test_results: List[Dict],
        extracted_json: Dict,
        iteration: int,
    ) -> str:
        return feedback_prompt_template.format(
            iteration=iteration,
            extracted_json=self.format_dict(extracted_json),
            test_results=self.format_dict(test_results),
            evaluation=evaluation,
        )
