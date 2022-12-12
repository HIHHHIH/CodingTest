import SaveIcon from "@mui/icons-material/Save";
import CodeEditor from "./CodeEditor";
import CodeDiff from "./CodeDiff";
import FolderIcon from "@mui/icons-material/Folder";
import RefreshIcon from "@mui/icons-material/Refresh";
import FileCopyIcon from "@mui/icons-material/FileCopy";
import SimCardDownloadIcon from "@mui/icons-material/SimCardDownload";
import ArrowBackIosNewIcon from "@mui/icons-material/ArrowBackIosNew";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import Button from "react-bootstrap/Button";
import {
  getProblemDetail,
  saveCodeInDB,
  executeCode,
  gradeCode,
  submitCode,
} from "../api/api";
import "./Center.scss";
import { useState } from "react";

const Center = (props) => {
  // codeDiff 에디터의 확장여부를 저장하는 변수
  const [codeDiffIsExpand, setCodeDiffIsExpand] = useState(0);

  // 제출 후 받은 정답 코드를 임시 저장하는 변수
  const [solutionCode, setSolutionCode] = useState("");

  const [tempCode, setTempCode] = useState("");

  const handleSaveCode = () => {
    // 코드를 슬롯에 저장하는 API요청. 저장 후 getProblemDetail을 실행
    saveCodeInDB(
      props.selectedProblemID,
      0,
      props.code,
      Number(props.selectedCode) + 1
    )
      .then((res) => {
        getProblemDetail(0, props.selectedProblemID)
          .then((res) => {
            props.setUserCode(res.data[2]);
          })
          .catch((err) => {
            console.log(err);
          });
        alert("Code Saved Successfully");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 코드슬롯을 변경하였을 경우 현재 선택된 코드슬롯 번호를 바꾸고 코드내용을 불러온다.
  const handleChangeCodeSlot = (event) => {
    props.setSelectedCode(Number(event.target.value));
    let flag = 0;
    props.userCode.map((code, index) => {
      if (code.code_idx === Number(event.target.value) + 1) {
        flag = 1;
        props.setCode(code.user_code);
        return;
      }
    });
    if (flag == 0) {
      props.setCode("");
    }
  };

  // 제출코드를 눌렀을 경우 현재 출력 코드를 제출된 코드내용으로 변경시킨다.
  const handleLoadSubmitCode = (event) => {
    let flag = 0;
    props.userCode.map((code, index) => {
      if (code.code_idx === Number(event.target.value) + 4) {
        flag = 1;
        props.setCode(code.user_code);
        return;
      }
    });
    if (flag == 0) {
      alert("No Submission Code Exist In This Slot");
    }
  };

  // 로컬에서 불러온 파일에서 텍스트를 읽는 함수
  const processFile = (file) => {
    var reader = new FileReader();
    reader.onload = function () {
      props.setCode(reader.result);
    };
    reader.readAsText(file /* optional */);
  };

  // 파일에서 코드 불러오기
  const handleLoadCode = () => {
    var input = document.createElement("input");
    input.type = "file";
    input.accept = "text/plain"; // 확장자가 xxx, yyy 일때, ".xxx, .yyy"
    input.onchange = function (event) {
      processFile(event.target.files[0]);
    };
    input.click();
  };

  // 코드 새로고침
  const handleRefreshCode = () => {
    props.setCode(props.skeletonCode);
  };

  // 코드 복사
  const handleCopyCode = async () => {
    try {
      await navigator.clipboard.writeText(props.code);
      alert("CODE Copyed successfully");
    } catch (err) {
      alert("CODE Copy failed");
    }
  };

  // 코드 텍스트 파일 형태로 다운로드
  const handleDownloadCode = () => {
    let fileName = `code_download.txt`;
    let output = props.code;
    const element = document.createElement("a");
    const file = new Blob([output], {
      type: "text/plain",
    });
    element.href = URL.createObjectURL(file);
    element.download = fileName;
    document.body.appendChild(element); // FireFox
    element.click();
  };

  // 코드 실행
  const handleExecuteCode = () => {
    props.setCodeEditorIsExpand(0);
    props.setRightSection(1);
    executeCode(props.code)
      .then((res) => {
        console.log(res.data);
        props.setExecuteResult(res.data.success);
        props.setExecuteMessage(res.data.message);
        if (!res.data.success) {
          props.setExecuteErrorLine(res.data.line_number);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 코드 채점
  const handleGradeCode = () => {
    props.setCodeEditorIsExpand(0);
    props.setRightSection(2);
    gradeCode(props.code, props.selectedProblemID)
      .then((res) => {
        console.log("채점결과: ", res.data);
        props.setGradeResult(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 코드 제출할 경우 코드를 저장하고 제출한다
  const handleSubmitCode = () => {
    props.setSubmittedWait(1);

    // 먼저 코드를 저장
    saveCodeInDB(
      props.selectedProblemID,
      0,
      props.code,
      Number(props.selectedCode) + 1
    )
      .then((res) => {
        getProblemDetail(0, props.selectedProblemID)
          .then((res) => {
            console.log("문제정보 가져오기 :", res.data);
            props.setUserCode(res.data[2]);
          })
          .catch((err) => {
            console.log(err);
          });
      })
      .catch((err) => {
        console.log(err);
      });

    // 이후 코드를 제출한다
    submitCode(
      props.selectedProblemID,
      0,
      props.code,
      Number(props.selectedCode) + 1
    )
      .then((res) => {
        if (res.data.result.msg === "no_submission_left") {
          alert("You have already submitted it 3 times. Cannot submit more.");
        } else if (res.data.result.msg === "fail") {
          alert("Your Code has an Error. Please check your code!");
        } else {
          setSolutionCode(res.data.solution_code);
          props.setCodeEditorIsExpand(0);
          if (props.isSubmitted2) {
            props.setCenterSection(2);
          }
          props.setRightSection(3);
          props.setSubmitResult(res.data);
        }
        props.setSubmittedWait(0);
      })
      .then(() => {
        getProblemDetail(0, props.selectedProblemID)
          .then((res) => {
            console.log("문제정보 가져오기 :", res.data);
            props.setUserCode(res.data[2]);
          })
          .catch((err) => {
            console.log(err);
          });
      })
      .catch((err) => {
        console.log(err);
        props.setSubmittedWait(0);
      });
  };

  // codeEditor 에디터 좌우로 확장
  const handleCodeEditorExpand = () => {
    props.setCodeEditorIsExpand(1);
  };

  // codeEditor 에디터 좌우로 축소
  const handleCodeEditorShrink = () => {
    props.setCodeEditorIsExpand(0);
  };

  // codeDiff 에디터 좌우로 확장
  const handleCodeDiffExpand = () => {
    setCodeDiffIsExpand(1);
  };

  // codeDiff 에디터 좌우로 축소
  const handleCodeDiffShrink = () => {
    setCodeDiffIsExpand(0);
  };

  // 제출 결과창에서 다시 코드 입력창으로 돌아가는 함수
  const handleGoBackToCode = () => {
    setCodeDiffIsExpand(0);
    props.setCenterSection(1);
    props.setRightSection(1);
  };

  console.log("현재 유저코드: ", props.userCode);

  if (props.centerSection == 1) {
    if (props.codeEditorIsExpand == 0) {
      return (
        <div className="center">
          <div className="centerHeader">
            Code Editor
            <SaveIcon
              type="button"
              style={{ margin: "auto 15px", color: "#FFFFFF" }}
              onClick={handleSaveCode}
              disabled={props.submittedWait}
            />
            <div className="centerSavedBox1">
              <div className="centerSavedBox1Title">Code Slot</div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic radio toggle button group"
              >
                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio1"
                  autocomplete="off"
                  value={0}
                  checked={props.selectedCode == 0}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio1">
                  1
                </label>

                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio2"
                  autocomplete="off"
                  value={1}
                  checked={props.selectedCode == 1}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio2">
                  2
                </label>

                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio3"
                  autocomplete="off"
                  value={2}
                  checked={props.selectedCode == 2}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio3">
                  3
                </label>
              </div>
            </div>
            <div className="centerSavedBox2">
              <div className="centerSavedBox2Title">Submitted</div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic outlined example"
              >
                <button
                  type="button"
                  class="btn btn-secondary"
                  value={0}
                  disabled={!props.isSubmitted1 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  1
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  value={1}
                  disabled={!props.isSubmitted2 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  2
                </button>
                <button
                  type="button"
                  class="btn btn-secondary"
                  value={2}
                  disabled={!props.isSubmitted3 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  3
                </button>
              </div>
            </div>
          </div>
          <div className="centerContent">
            <Button
              variant="secondary"
              style={{
                position: "absolute",
                bottom: "10px",
                right: "10px",
                zIndex: 1,
              }}
              onClick={handleCodeEditorExpand}
              disabled={props.submittedWait}
            >
              <ArrowForwardIosIcon />
            </Button>
            <CodeEditor code={props.code} setCode={props.setCode} />
          </div>
          <div className="centerFooter">
            <div className="centerFooter1">
              <FolderIcon
                type="button"
                style={{ marginRight: "5px", color: "#FFFFFF" }}
                onClick={handleLoadCode}
                disabled={props.submittedWait}
              />
              <RefreshIcon
                type="button"
                style={{ marginRight: "5px", color: "#FFFFFF" }}
                onClick={handleRefreshCode}
                disabled={props.submittedWait}
              />
              <FileCopyIcon
                type="button"
                style={{ marginRight: "5px", color: "#FFFFFF" }}
                onClick={handleCopyCode}
                disabled={props.submittedWait}
              />
              <SimCardDownloadIcon
                type="button"
                style={{ color: "#FFFFFF" }}
                onClick={handleDownloadCode}
                disabled={props.submittedWait}
              />
            </div>
            <div className="centerFooter2">
              <Button
                variant="secondary"
                style={{
                  marginRight: "10px",
                }}
                onClick={handleExecuteCode}
                disabled={props.submittedWait}
              >
                Execute
              </Button>
              <Button
                variant="secondary"
                style={{
                  marginRight: "10px",
                }}
                onClick={handleGradeCode}
                disabled={props.submittedWait}
              >
                Score
              </Button>
              <Button
                variant="secondary"
                onClick={handleSubmitCode}
                disabled={props.submittedWait}
              >
                Submit
              </Button>
            </div>
          </div>
        </div>
      );
    } else {
      return (
        <div className="centerEx">
          <div className="centerExHeader">
            Code Editor
            <SaveIcon
              type="button"
              style={{ margin: "auto 15px auto auto", color: "#FFFFFF" }}
              onClick={handleSaveCode}
              disabled={props.submittedWait}
            />
            <div className="centerSavedBox1">
              <div className="centerSavedBox1Title">Code Slot</div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic radio toggle button group"
              >
                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio1"
                  autocomplete="off"
                  value={0}
                  checked={props.selectedCode == 0}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio1">
                  1
                </label>

                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio2"
                  autocomplete="off"
                  value={1}
                  checked={props.selectedCode == 1}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio2">
                  2
                </label>

                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="btnradio3"
                  autocomplete="off"
                  value={2}
                  checked={props.selectedCode == 2}
                  onClick={handleChangeCodeSlot}
                  disabled={props.submittedWait}
                />
                <label class="btn btn-outline-secondary" for="btnradio3">
                  3
                </label>
              </div>
            </div>
            <div className="centerSavedBox2">
              <div className="centerSavedBox2Title">Submitted</div>
              <div
                class="btn-group"
                role="group"
                aria-label="Basic outlined example"
              >
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  value={0}
                  disabled={!props.isSubmitted1 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  1
                </button>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  value={1}
                  disabled={!props.isSubmitted2 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  2
                </button>
                <button
                  type="button"
                  class="btn btn-outline-secondary"
                  value={2}
                  disabled={!props.isSubmitted3 || props.submittedWait}
                  onClick={handleLoadSubmitCode}
                >
                  3
                </button>
              </div>
            </div>
          </div>
          <div className="centerExContent">
            <Button
              variant="secondary"
              style={{
                position: "absolute",
                bottom: "10px",
                right: "10px",
                zIndex: 1,
              }}
              onClick={handleCodeEditorShrink}
              disabled={props.submittedWait}
            >
              <ArrowBackIosNewIcon />
            </Button>
            <CodeEditor code={props.code} setCode={props.setCode} />
          </div>
          <div className="centerExFooter">
            <FolderIcon
              type="button"
              style={{ marginRight: "10px", color: "#FFFFFF" }}
              onClick={handleLoadCode}
              disabled={props.submittedWait}
            />
            <RefreshIcon
              type="button"
              style={{ marginRight: "10px", color: "#FFFFFF" }}
              onClick={handleRefreshCode}
              disabled={props.submittedWait}
            />
            <FileCopyIcon
              type="button"
              style={{ marginRight: "10px", color: "#FFFFFF" }}
              onClick={handleCopyCode}
              disabled={props.submittedWait}
            />
            <SimCardDownloadIcon
              type="button"
              style={{ marginRight: "auto", color: "#FFFFFF" }}
              onClick={handleDownloadCode}
              disabled={props.submittedWait}
            />
            <Button
              variant="secondary"
              style={{
                marginRight: "10px",
              }}
              onClick={handleExecuteCode}
              disabled={props.submittedWait}
            >
              Execute
            </Button>
            <Button
              variant="secondary"
              style={{
                marginRight: "10px",
              }}
              onClick={handleGradeCode}
              disabled={props.submittedWait}
            >
              Score
            </Button>
            <Button
              variant="secondary"
              onClick={handleSubmitCode}
              disabled={props.submittedWait}
            >
              Submit
            </Button>
          </div>
        </div>
      );
    }
  } else {
    if (codeDiffIsExpand == 0) {
      return (
        <div className="center2">
          <div className="center2Header">
            Code Diff : Submitted Code Analysis
          </div>
          <div className="center2Content">
            <Button
              variant="secondary"
              style={{
                position: "absolute",
                bottom: "10px",
                left: "10px",
                zIndex: 1,
              }}
              onClick={handleCodeDiffExpand}
            >
              <ArrowBackIosNewIcon />
            </Button>
            <CodeDiff
              code={props.code}
              solutionCode={solutionCode}
              expanded={false}
            />
          </div>
          <div className="center2Footer">
            <Button
              variant="secondary"
              style={{
                marginRight: "10px",
              }}
              onClick={handleGoBackToCode}
              disabled={props.submittedWait}
            >
              Go Back To Editor
            </Button>
          </div>
        </div>
      );
    } else {
      return (
        <div className="center2Ex">
          <div className="center2ExHeader">
            Code Diff : Submitted Code Analysis
          </div>
          <div className="center2ExContent">
            <Button
              variant="secondary"
              style={{
                position: "absolute",
                bottom: "10px",
                left: "10px",
                zIndex: 1,
              }}
              onClick={handleCodeDiffShrink}
            >
              <ArrowForwardIosIcon />
            </Button>
            <CodeDiff
              code={props.code}
              solutionCode={solutionCode}
              expanded={true}
            />
          </div>
          <div className="center2ExFooter">
            <Button
              variant="secondary"
              style={{
                marginRight: "10px",
              }}
              onClick={handleGoBackToCode}
              disabled={props.submittedWait}
            >
              Go Back To Editor
            </Button>
          </div>
        </div>
      );
    }
  }
};

export default Center;
