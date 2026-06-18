import io
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from texttest_fixture import main
from approvaltests import verify


def Test_Approvals():
    orig_sysout = sys.stdout
    try:
        fake_stdout = io.StringIO()
        sys.stdout = fake_stdout
        sys.argv = ["texttest_fixture.py", 30]
        main()
        answer = fake_stdout.getvalue()
    finally:
        sys.stdout = orig_sysout

    verify(answer)

if __name__ == "__main__":
    Test_Approvals()