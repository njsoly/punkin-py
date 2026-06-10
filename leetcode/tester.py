## CLAUDE DISCLAIMER - I didn't want to figure out all this fancy stuff. ##

"""Tiny reusable tester: call a function with any args and print input/output.

Usage:
	from tester import show_call
	show_call(my_func, arg1, arg2, kw=value)
"""
from typing import Any, Callable, Iterable, Sequence


def _format_args(args: tuple, kwargs: dict) -> str:
	parts = [repr(a) for a in args]
	parts += [f'{k}={v!r}' for k, v in kwargs.items()]
	return ', '.join(parts)


def show_call(func: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
	"""Call `func` with the given args/kwargs, print the call and result, return result."""
	rendered = _format_args(args, kwargs)
	try:
		result = func(*args, **kwargs)
	except Exception as e:
		tb = e.__traceback__
		# Walk to the deepest frame (actual throw point)
		last = tb
		while last and last.tb_next:
			last = last.tb_next
		if last is not None:
			frame = last.tb_frame
			loc = f' at {frame.f_code.co_filename}:{last.tb_lineno} in {frame.f_code.co_name}'
		else:
			loc = ''
		print(f'{func.__name__}({rendered}) raised {type(e).__name__}: {e}{loc}')
		raise
	print(f'{func.__name__}({rendered}) = {result!r}')
	return result


def run_test_cases(
		approaches: Iterable[Callable[..., Any]],
		test_cases: Sequence[tuple[tuple, Any]],
) -> int:
	"""Run each approach against every (args, expected) test case via `show_call`.

	`test_cases` is a sequence of ((arg1, arg2, ...), expected) pairs.
	Prints OK/FAIL per case and returns the total number of failures.
	"""
	failures = 0
	for approach in approaches:
		print(f'Approach: {approach.__name__}')
		for args, expected in test_cases:
			result = show_call(approach, *args)
			if result == expected:
				status = 'OK'
			else:
				status = f'FAIL (expected {expected!r})'
				failures += 1
			print(f'  -> {status}')
	return failures


if __name__ == '__main__':
	# self-test
	show_call(sum, [1, 2, 3])
	show_call(max, 4, 9, 2)
	show_call(sorted, [3, 1, 2], reverse=True)
