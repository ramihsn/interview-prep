from typing import BinaryIO
from io import StringIO
import csv
import re

from app.schemas.questions import QuestionCreate


async def from_csv_file(file: BinaryIO) -> list[QuestionCreate]:
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents a row.

    Args:
        file: The file-like object of the uploaded CSV.

    Returns:
        A list of dictionaries containing the CSV data.
    """
    # Read the file content
    content = file.read()

    # Decode the file content (assuming UTF-8 encoding)
    decoded_content = content.decode('utf-8')
    if not re.match(r'\s*topic\s*,\s*difficulty\s*,\s*question\s*\n', decoded_content, re.I):
        raise ValueError(
            "Invalid CSV file format, expected titles (first row): 'topic', 'difficulty', 'question'"
        )

    # Use StringIO to create a file-like object from the string content
    csv_reader = csv.DictReader(StringIO(decoded_content))

    # Convert the CSV reader to a list of QuestionCreate objects
    questions = [QuestionCreate(**row) for row in csv_reader]

    return questions
