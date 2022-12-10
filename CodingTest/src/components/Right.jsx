import { useState, useEffect } from "react";
import PublishedWithChangesIcon from "@mui/icons-material/PublishedWithChanges";
import {
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  Legend,
  Bar,
} from "recharts";
import AssignmentIcon from "@mui/icons-material/Assignment";
import "./Right.scss";

const Right = (props) => {
  // 채점 결과 점수와 테스트케이스 1,2,3(오픈), 4,5,6(히든)의 결과와 입/출력, 사용자 출력값을 저장하는 변수
  const [gradeScore, setGradeScore] = useState(0);
  const [testcase1Result, setTestcase1Result] = useState("");
  const [testcase1Input, setTestcase1Input] = useState("");
  const [testcase1CorrectOutput, setTestcase1CorrectOutput] = useState("");
  const [testcase1UserOutput, setTestcase1UserOutput] = useState("");

  const [testcase2Result, setTestcase2Result] = useState("");
  const [testcase2Input, setTestcase2Input] = useState("");
  const [testcase2CorrectOutput, setTestcase2CorrectOutput] = useState("");
  const [testcase2UserOutput, setTestcase2UserOutput] = useState("");

  const [testcase3Result, setTestcase3Result] = useState("");
  const [testcase4Result, setTestcase4Result] = useState("");
  const [testcase5Result, setTestcase5Result] = useState("");

  // 제출 결과를 저장하는 변수들
  const [submitData, setSubmitData] = useState([
    { name: "criterion", score: 100 },
  ]);
  const [submitResultCodex, setSubmitResultCodex] = useState("");

  const [submitResultMultimetricOutput1, setSubmitResultMultimetricOutput1] =
    useState(0);
  const [submitResultMultimetricOutput2, setSubmitResultMultimetricOutput2] =
    useState(0);
  const [submitResultMultimetricOutput3, setSubmitResultMultimetricOutput3] =
    useState(0);
  const [submitResultMultimetricOutput4, setSubmitResultMultimetricOutput4] =
    useState(0);

  const [submitResultPlagiarism, setSubmitResultPlagiarism] = useState(0);

  const [submitResultPylama1Score, setSubmitResultPylama1Score] = useState(0);
  const [submitResultPylama1Message, setSubmitResultPylama1Message] = useState(
    []
  );
  const [submitResultPylama2Score, setSubmitResultPylama2Score] = useState(0);
  const [submitResultPylama2Message, setSubmitResultPylama2Message] = useState(
    []
  );
  const [submitResultPylama3Score, setSubmitResultPylama3Score] = useState(0);
  const [submitResultPylama3Message, setSubmitResultPylama3Message] = useState(
    []
  );
  const [submitResultPylama4Score, setSubmitResultPylama4Score] = useState(0);
  const [submitResultPylama4Message, setSubmitResultPylama4Message] = useState(
    []
  );
  const [submitResultPylama5Score, setSubmitResultPylama5Score] = useState(0);
  const [submitResultPylama5Message, setSubmitResultPylama5Message] = useState(
    []
  );

  const [submitResultReference, setSubmitResultReference] = useState([]);

  const [submitResultSolutionCode, setSubmitResultSolutionCode] = useState("");

  const [submitResultGradeScore, setSubmitResultGradeScore] = useState(0);
  const [submitResultTestcase1Result, setSubmitResultTestcase1Result] =
    useState("");
  const [submitResultTestcase1Input, setSubmitResultTestcase1Input] =
    useState("");
  const [submitResultTestcase1Output, setSubmitResultTestcase1Output] =
    useState("");
  const [submitResultTestcase1UserOutput, setSubmitResultTestcase1UserOutput] =
    useState("");

  const [submitResultTestcase2Result, setSubmitResultTestcase2Result] =
    useState("");
  const [submitResultTestcase2Input, setSubmitResultTestcase2Input] =
    useState("");
  const [submitResultTestcase2Output, setSubmitResultTestcase2Output] =
    useState("");
  const [submitResultTestcase2UserOutput, setSubmitResultTestcase2UserOutput] =
    useState("");

  const [submitResultTestcase3Result, setSubmitResultTestcase3Result] =
    useState("");
  const [submitResultTestcase4Result, setSubmitResultTestcase4Result] =
    useState("");
  const [submitResultTestcase5Result, setSubmitResultTestcase5Result] =
    useState("");

  // 제출결과 현재페이지(제출결과/코드설명,관련자료)를 저장하는 변수
  const [submitResultPage, setSubmitResultPage] = useState(0);
  const [submitResultPage1Content, setSubmitResultPage1Content] = useState(0);

  // 채점 시 첫번째 테스트 케이스의 조건부 렌더링 함수
  const gradeResult1 = () => {
    if (testcase1Result == "실패") {
      return (
        <div style={{ paddingLeft: "30px" }}>
          Input : {testcase1Input}
          <br />
          Expected Output : {testcase1CorrectOutput}
          <br />
          Your Output : {testcase1UserOutput}
        </div>
      );
    }
  };

  // 채점 시 두번째 테스트 케이스의 조건부 렌더링 함수
  const gradeResult2 = () => {
    if (testcase2Result == "실패") {
      return (
        <div style={{ paddingLeft: "30px" }}>
          Input : {testcase2Input}
          <br />
          Expected Output : {testcase2CorrectOutput}
          <br />
          Your Output : {testcase2UserOutput}
        </div>
      );
    }
  };

  // 제출 시 첫번째 테스트 케이스의 조건부 렌더링 함수
  const submitGradeResult1 = () => {
    if (submitResultTestcase1Result == "실패") {
      return (
        <div style={{ paddingLeft: "30px" }}>
          Input : {submitResultTestcase1Input}
          <br />
          Expected Output : {submitResultTestcase1Output}
          <br />
          Your Output : {submitResultTestcase1UserOutput}
        </div>
      );
    }
  };

  // 제출 시 두번째 테스트 케이스의 조건부 렌더링 함수
  const submitGradeResult2 = () => {
    if (submitResultTestcase2Result == "실패") {
      return (
        <div style={{ paddingLeft: "30px" }}>
          Input : {submitResultTestcase2Input}
          <br />
          Expected Output : {submitResultTestcase2Output}
          <br />
          Your Output : {submitResultTestcase2UserOutput}
        </div>
      );
    }
  };

  // 표절율을 렌더링하는 함수
  const handlePlagiarism = () => {
    if (submitResultPlagiarism <= 0.5) {
      return (
        <p
          style={{
            position: "absolute",
            top: "10px",
            left: "10px",
            color: "#39C330",
            fontWeight: "700",
          }}
        >
          표절율: {submitResultPlagiarism.toFixed(2) * 100}%
        </p>
      );
    } else {
      return (
        <p
          style={{
            position: "absolute",
            top: "10px",
            left: "10px",
            color: "#FF2300",
            fontWeight: "700",
          }}
        >
          표절율: {submitResultPlagiarism.toFixed(2) * 100}%
        </p>
      );
    }
  };

  // 제출결과를 렌더링하는 함수
  const handleSubmitResult = () => {
    if (submitResultPage === 0) {
      return (
        <div className="submitResult1">
          {handlePlagiarism()}
          <PublishedWithChangesIcon
            type="button"
            style={{ position: "absolute", top: "10px", right: "0" }}
            onClick={handleChangeResultMode}
            disabled={props.submittedWait}
          />
          <div className="submitResult1Header">
            총점:{" "}
            {submitResultGradeScore +
              submitResultMultimetricOutput1 +
              submitResultMultimetricOutput2 +
              submitResultMultimetricOutput3 +
              submitResultMultimetricOutput4 +
              submitResultPylama1Score +
              submitResultPylama2Score +
              submitResultPylama3Score +
              submitResultPylama4Score +
              submitResultPylama5Score}
            점 / 300점
          </div>
          <div className="submitResult1Graph">
            <BarChart
              width={388}
              height={250}
              data={submitData}
              style={{ backgroundColor: "#E2E2E2" }}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="score" fill="#8884d8" />
            </BarChart>
          </div>
          <div className="submitResult1Tap">
            <div class="btn-group" role="group" aria-label="Basic example">
              <button
                type="button"
                class="btn btn-secondary"
                value={0}
                onClick={handleSubmitContentChange}
                disabled={props.submittedWait}
              >
                기능점수확인
              </button>
              <button
                type="button"
                class="btn btn-secondary"
                value={1}
                onClick={handleSubmitContentChange}
                disabled={props.submittedWait}
              >
                효율점수확인
              </button>
              <button
                type="button"
                class="btn btn-secondary"
                value={2}
                onClick={handleSubmitContentChange}
                disabled={props.submittedWait}
              >
                가독성점수확인
              </button>
            </div>
          </div>
          <div className="submitResult1Content">{handleSubmitContent()}</div>
        </div>
      );
    } else {
      return (
        <div className="submitResult2">
          <div className="submitResult2Header">
            코드 설명 & 관련 자료
            <PublishedWithChangesIcon
              type="button"
              style={{ position: "absolute", top: "10px", right: "0" }}
              onClick={handleChangeResultMode}
            />
          </div>
          <div className="submitResult2Content">
            <AssignmentIcon />
            &nbsp;code explanation: <br />
            <div style={{ paddingLeft: "30px" }}>{submitResultCodex}</div>
            <br />
            <br />
            <AssignmentIcon />
            &nbsp;useful materials:
            <br />
            {submitResultReference.map((reference) => {
              return (
                <>
                  <a
                    href={reference.url}
                    target="blank"
                    style={{ paddingLeft: "30px" }}
                  >
                    {reference.title}
                  </a>
                  <br />
                </>
              );
            })}
          </div>
        </div>
      );
    }
  };

  // 채점결과 페이지(제출결과, 코드설명/관련자료) 바꾸는 함수
  const handleChangeResultMode = () => {
    if (submitResultPage === 0) {
      setSubmitResultPage(1);
    } else {
      setSubmitResultPage(0);
    }
  };

  // 채점결과 중 제출결과 표시내용(기능점수, 효율점수, 가독성점수) 바꾸는 함수
  const handleSubmitContentChange = (event) => {
    setSubmitResultPage1Content(event.target.value);
  };

  // 채점결과 중 기능점수, 효율점수, 가독성점수를 렌더링하는 함수
  const handleSubmitContent = () => {
    if (submitResultPage1Content == 0) {
      return (
        <div className="submitContent1">
          <AssignmentIcon />
          &nbsp;총점 {submitResultGradeScore}점<br />
          <br />
          <AssignmentIcon />
          &nbsp;테스트케이스-1: {submitResultTestcase1Result}
          {submitGradeResult1()}
          <br />
          <br />
          <AssignmentIcon />
          &nbsp;테스트케이스-2: {submitResultTestcase2Result}
          {submitGradeResult2()}
          <br />
          <br />
          <AssignmentIcon />
          &nbsp;히든 테스트케이스-3: {submitResultTestcase3Result}
          <br />
          <br />
          <AssignmentIcon />
          &nbsp;히든 테스트케이스-4: {submitResultTestcase4Result}
          <br />
          <br />
          <AssignmentIcon />
          &nbsp;히든 테스트케이스-5: {submitResultTestcase5Result}
        </div>
      );
    } else if (submitResultPage1Content == 1) {
      return (
        <div className="submitContent2">
          <div>
            <AssignmentIcon />
            &nbsp;control complexity score: {submitResultMultimetricOutput1}
          </div>
          <br />
          <div>
            <AssignmentIcon />
            &nbsp;data complexity score: {submitResultMultimetricOutput2}
          </div>
          <br />{" "}
          <div>
            <AssignmentIcon />
            &nbsp;halstead score: {submitResultMultimetricOutput3}
          </div>
          <br />{" "}
          <div>
            <AssignmentIcon />
            &nbsp;loc score: {submitResultMultimetricOutput4}
          </div>
        </div>
      );
    } else {
      return (
        <div className="submitContent3">
          <div>
            <AssignmentIcon />
            &nbsp;eradicate score: {submitResultPylama1Score}
          </div>
          {submitResultPylama1Message.map((message) => {
            return <div style={{ paddingLeft: "30px" }}>{message}</div>;
          })}
          <br />
          <div>
            <AssignmentIcon />
            &nbsp;mypy score: {submitResultPylama2Score}
          </div>
          {submitResultPylama2Message.map((message) => {
            return <div style={{ paddingLeft: "30px" }}>{message}</div>;
          })}
          <br />{" "}
          <div>
            <AssignmentIcon />
            &nbsp;pycodestyle score: {submitResultPylama3Score}
          </div>
          {submitResultPylama3Message.map((message) => {
            return <div style={{ paddingLeft: "30px" }}>{message}</div>;
          })}
          <br />{" "}
          <div>
            <AssignmentIcon />
            &nbsp;pylint score: {submitResultPylama4Score}
          </div>
          {submitResultPylama4Message.map((message) => {
            return <div style={{ paddingLeft: "30px" }}>{message}</div>;
          })}
          <br />{" "}
          <div>
            <AssignmentIcon />
            &nbsp;radon score: {submitResultPylama5Score}
          </div>
          {submitResultPylama5Message.map((message) => {
            return <div style={{ paddingLeft: "30px" }}>{message}</div>;
          })}
        </div>
      );
    }
  };

  // 채점결과가 변경될 때마다 채점 관련 변수들을 변경
  useEffect(() => {
    if (
      props.gradeResult !== undefined &&
      props.gradeResult !== {} &&
      props.gradeResult.open_results !== undefined &&
      props.gradeResult.hidden_results !== undefined
    ) {
      setGradeScore(props.gradeResult.score);
      setTestcase1Result(props.gradeResult.open_results[0].result);
      setTestcase1Input(props.gradeResult.open_results[0].input);
      setTestcase1CorrectOutput(
        props.gradeResult.open_results[0].correct_output
      );
      setTestcase1UserOutput(props.gradeResult.open_results[0].your_output);

      setTestcase2Result(props.gradeResult.open_results[1].result);
      setTestcase2Input(props.gradeResult.open_results[1].input);
      setTestcase2CorrectOutput(
        props.gradeResult.open_results[1].correct_output
      );
      setTestcase2UserOutput(props.gradeResult.open_results[1].your_output);

      setTestcase3Result(props.gradeResult.hidden_results[0].result);
      setTestcase4Result(props.gradeResult.hidden_results[1].result);
      setTestcase5Result(props.gradeResult.hidden_results[2].result);
    }
  }, [props.gradeResult]);

  // 제출결과가 변경될 때마다 제출 관련 변수들을 변경
  useEffect(() => {
    if (
      props.submitResult !== undefined &&
      props.submitResult !== {} &&
      props.submitResult.codex_output !== undefined
    ) {
      console.log("제출결과: ", props.submitResult);
      setSubmitResultCodex(props.submitResult.codex_output);

      setSubmitResultMultimetricOutput1(
        props.submitResult.multimetric_output.control_complexity_score
      );
      setSubmitResultMultimetricOutput2(
        props.submitResult.multimetric_output.data_complexity_score
      );
      setSubmitResultMultimetricOutput3(
        props.submitResult.multimetric_output.halstead_score
      );
      setSubmitResultMultimetricOutput4(
        props.submitResult.multimetric_output.loc_score
      );

      setSubmitResultPlagiarism(props.submitResult.plagiarism.plagiarism_rate);

      setSubmitResultPylama1Score(
        props.submitResult.pylama_output.eradicate.score
      );
      setSubmitResultPylama1Message(
        props.submitResult.pylama_output.eradicate.msg
      );
      setSubmitResultPylama2Score(props.submitResult.pylama_output.mypy.score);
      setSubmitResultPylama2Message(props.submitResult.pylama_output.mypy.msg);
      setSubmitResultPylama3Score(
        props.submitResult.pylama_output.pycodestyle.score
      );
      setSubmitResultPylama3Message(
        props.submitResult.pylama_output.pycodestyle.msg
      );
      setSubmitResultPylama4Score(
        props.submitResult.pylama_output.pylint.score
      );
      setSubmitResultPylama4Message(
        props.submitResult.pylama_output.pylint.msg
      );
      setSubmitResultPylama5Score(props.submitResult.pylama_output.radon.score);
      setSubmitResultPylama5Message(props.submitResult.pylama_output.radon.msg);

      setSubmitResultReference(props.submitResult.reference);

      setSubmitResultSolutionCode(props.submitResult.solution_code);

      setSubmitResultGradeScore(props.submitResult.testcase_output.score);
      setSubmitResultTestcase1Result(
        props.submitResult.testcase_output.open_results[0].result
      );
      setSubmitResultTestcase1Input(
        props.submitResult.testcase_output.open_results[0].input
      );
      setSubmitResultTestcase1Output(
        props.submitResult.testcase_output.open_results[0].correct_output
      );
      setSubmitResultTestcase1UserOutput(
        props.submitResult.testcase_output.open_results[0].your_output
      );

      setSubmitResultTestcase2Result(
        props.submitResult.testcase_output.open_results[1].result
      );
      setSubmitResultTestcase2Input(
        props.submitResult.testcase_output.open_results[1].input
      );
      setSubmitResultTestcase2Output(
        props.submitResult.testcase_output.open_results[1].correct_output
      );
      setSubmitResultTestcase2UserOutput(
        props.submitResult.testcase_output.open_results[1].your_output
      );

      setSubmitResultTestcase3Result(
        props.submitResult.testcase_output.hidden_results[0].result
      );
      setSubmitResultTestcase4Result(
        props.submitResult.testcase_output.hidden_results[1].result
      );
      setSubmitResultTestcase5Result(
        props.submitResult.testcase_output.hidden_results[2].result
      );

      setSubmitResultPage(0);
      setSubmitResultPage1Content(0);
    }
  }, [props.submitResult]);

  // 제출 결과 중 점수들이 바뀔 때마다 그래프 데이터를 갱신해준다
  useEffect(() => {
    setSubmitData([
      { name: "function", score: submitResultGradeScore },
      {
        name: "efficiency",
        score:
          submitResultMultimetricOutput1 +
          submitResultMultimetricOutput2 +
          submitResultMultimetricOutput3 +
          submitResultMultimetricOutput4,
      },
      {
        name: "readability",
        score:
          submitResultPylama1Score +
          submitResultPylama2Score +
          submitResultPylama3Score +
          submitResultPylama4Score +
          submitResultPylama5Score,
      },
    ]);
  }, [
    submitResultGradeScore,
    submitResultMultimetricOutput1,
    submitResultMultimetricOutput2,
    submitResultMultimetricOutput3,
    submitResultMultimetricOutput4,
    submitResultPylama1Score,
    submitResultPylama2Score,
    submitResultPylama3Score,
    submitResultPylama4Score,
    submitResultPylama5Score,
  ]);

  // 사용자가 실행버튼을 누르면 실행화면을 보여준다
  if (props.rightSection == 1) {
    return (
      <div className="right1">
        <div className="right1Header">Execution Result</div>
        <div className="right1Content">{props.excuteMessage}</div>
      </div>
    );
  }

  // 사용자가 채점버튼을 누르면 채점화면을 보여준다
  else if (props.rightSection == 2) {
    return (
      <div className="right2">
        <div className="right2Header">Score Result</div>
        <div className="right2Content">
          총점&nbsp;{gradeScore}점<br />
          <br />
          테스트케이스-1: {testcase1Result}
          {gradeResult1()}
          <br />
          <br />
          테스트케이스-2: {testcase2Result}
          {gradeResult2()}
          <br />
          <br />
          히든 테스트케이스-3: {testcase3Result}
          <br />
          <br />
          히든 테스트케이스-4: {testcase4Result}
          <br />
          <br />
          히든 테스트케이스-5: {testcase5Result}
        </div>
      </div>
    );
  }

  // 사용자가 제출버튼을 누르면 제출하면을 보여준다
  else {
    return (
      <div className="right3">
        <div className="right3Header">Submit Result</div>
        <div className="right3Content">{handleSubmitResult()}</div>
      </div>
    );
  }
};

export default Right;
