def compare_answers(expected: str, generated: str) -> bool:
	"""Return True when two answers match after basic normalization."""
	normalized_expected = expected.strip().lower()
	normalized_generated = generated.strip().lower()

	return normalized_expected == normalized_generated


if __name__ == "__main__":
	print(compare_answers("Paris", "Paris"))
	print(compare_answers("Paris", " paris "))
	print(compare_answers("Paris", "London"))
