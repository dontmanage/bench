VERSION = "5.16.2"
PROJECT_NAME = "dontmanage-bench"
DONTMANAGE_VERSION = None
current_path = None
updated_path = None
LOG_BUFFER = []


def set_dontmanage_version(bench_path="."):
	from .utils.app import get_current_dontmanage_version

	global DONTMANAGE_VERSION
	if not DONTMANAGE_VERSION:
		DONTMANAGE_VERSION = get_current_dontmanage_version(bench_path=bench_path)
