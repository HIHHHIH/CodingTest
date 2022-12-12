import { useState, useEffect } from "react";
import { runTestcase } from "../api/api";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import "./Left.scss";

const Left = (props) => {
  const [problemContent, setProblemContent] = useState("");
  const [problemConstraint, setProblemConstraint] = useState("");
  const [showedTestcase1Input, setShowedTestcase1Input] = useState("");
  const [showedTestcase1Output, setShowedTestcase1Output] = useState("");
  const [showedTestcase1Result, setShowedTestcase1Result] = useState("");
  const [showedTestcase1YourOutput, setShowedTestcase1YourOutput] =
    useState("");
  const [showedTestcase2Input, setShowedTestcase2Input] = useState("");
  const [showedTestcase2Output, setShowedTestcase2Output] = useState("");
  const [showedTestcase2Result, setShowedTestcase2Result] = useState("");
  const [showedTestcase2YourOutput, setShowedTestcase2YourOutput] =
    useState("");

  const handleChangeProblem = (event) => {
    props.setSelectedProblemIndex(event.target.value);
    props.setSelectedProblemID(props.problem[event.target.value].problem_id);
  };

  const handleVerifyTestcase1 = (event) => {
    runTestcase(props.code, showedTestcase1Input, showedTestcase1Output)
      .then((res) => {
        console.log("검증결과: ", res.data);
        if (res.data.result == "P") {
          setShowedTestcase1Result("PASS");
          setShowedTestcase1YourOutput(res.data.output);
        } else {
          setShowedTestcase1Result("FAIL");
          setShowedTestcase1YourOutput(res.data.output);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleVerifyTestcase2 = (event) => {
    runTestcase(props.code, showedTestcase2Input, showedTestcase2Output)
      .then((res) => {
        if (res.data.result == "P") {
          setShowedTestcase2Result("PASS");
          setShowedTestcase2YourOutput(res.data.output);
        } else {
          setShowedTestcase2Result("FAIL");
          setShowedTestcase2YourOutput(res.data.output);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 문제배열과 선택 문제 인덱스가 바뀔 때마다 문제 목록과 선택된 문제 인덱스를 받아와서 제목, 내용, 제약조건 설정
  useEffect(() => {
    if (
      props.problem !== undefined &&
      props.problem[props.selectedProblemIndex] !== undefined
    ) {
      setProblemContent(props.problem[props.selectedProblemIndex].description);
      setProblemConstraint(
        props.problem[props.selectedProblemIndex].restriction
      );
    }
  }, [props.problem, props.selectedProblemIndex]);

  // 테스트케이스배열이 바뀔 때마다 테스트케이스 0번, 1번 인덱스의 입출력 추출 및 검증결과, 사용자 출력 초기화
  useEffect(() => {
    if (props.testcase !== undefined && props.testcase.length >= 1) {
      setShowedTestcase1Input(props.testcase[0].input);
      setShowedTestcase1Output(props.testcase[0].output);
      setShowedTestcase2Input(props.testcase[1].input);
      setShowedTestcase2Output(props.testcase[1].output);
      setShowedTestcase1Result("");
      setShowedTestcase2Result("");
      setShowedTestcase1YourOutput("");
      setShowedTestcase2YourOutput("");
    }
  }, [props.testcase, props.selectedCode]);

  return (
    <div className="left">
      <div className="problem">
        <div className="problemHeader">
          Problem :
          <FormControl sx={{ m: 1, width: "75%" }} size="small">
            <InputLabel
              id="demo-select-small"
              style={{ color: "#000000" }}
            ></InputLabel>
            <Select
              labelId="demo-select-small"
              id="demo-select-small"
              value={props.selectedProblemIndex}
              label="Age"
              style={{ backgroundColor: "#FFFFFF" }}
              onChange={handleChangeProblem}
              disabled={props.submittedWait}
            >
              {props.problem.map((problem, index) => {
                return <MenuItem value={index}>{problem.title}</MenuItem>;
              })}
            </Select>
          </FormControl>
        </div>
        <div className="problemContent">
          <div className="problemContentText">{problemContent}</div>
        </div>
        <div className="problemConstraint">
          <div className="problemConstraintHeader">Reference/Constraint</div>
          <div className="problemConstraintText">{problemConstraint}</div>
        </div>
      </div>
      <div className="testcase">
        <div className="testcaseHeader">Testcase :</div>
        <div className="testcase1">
          <div className="testcase1Header">
            Testcase-1
            <button
              type="button"
              class="btn btn-secondary btn-sm"
              style={{ float: "right", marginRight: "10px" }}
              onClick={handleVerifyTestcase1}
              disabled={props.submittedWait}
            >
              Verify
            </button>
          </div>
          <div className="testcase1Content">
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>Input :</div>
              <div>Expected Output :</div>
            </div>
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%", color: "#6187FF" }}>
                {showedTestcase1Input}
              </div>
              <div style={{ width: "40%", color: "#FF5A5A" }}>
                {showedTestcase1Output}
              </div>
            </div>
            <br />
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>PASS/FAIL :</div>
              <div>Your Output :</div>
            </div>
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>{showedTestcase1Result}</div>
              <div>{showedTestcase1YourOutput}</div>
            </div>
          </div>
        </div>
        <div className="testcase2">
          <div className="testcase2Header">
            Testcase-2
            <button
              type="button"
              class="btn btn-secondary btn-sm"
              style={{ float: "right", marginRight: "10px" }}
              onClick={handleVerifyTestcase2}
              disabled={props.submittedWait}
            >
              Verify
            </button>
          </div>
          <div className="testcase2Content">
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>Input :</div>
              <div>Expected Output :</div>
            </div>
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%", color: "#6187FF" }}>
                {showedTestcase2Input}
              </div>
              <div style={{ width: "40%", color: "#FF5A5A" }}>
                {showedTestcase2Output}
              </div>
            </div>
            <br />
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>PASS/FAIL :</div>
              <div>Your Output :</div>
            </div>
            <div style={{ display: "flex" }}>
              <div style={{ width: "45%" }}>{showedTestcase2Result}</div>
              <div>{showedTestcase2YourOutput}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Left;
