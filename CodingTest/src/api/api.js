import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: false,
});

const getLecture = async () => {
  return await instance.post("/study/");
};

const getAssignment = async (lecture_id) => {
  return await instance.post("/study/lecture/", {
    lecture_id,
  });
};

const getProblems = async (lecture_id, assignment_id) => {
  return await instance.post("/study/assignment/", {
    lecture_id,
    assignment_id,
  });
};

const getProblem = async (lecture_id, assignment_id, problem_id) => {
  return await instance.post("/study/problem/", {
    lecture_id,
    assignment_id,
    problem_id,
  });
};

const getProblemDetail = async (user_id, problem_id) => {
  return await instance.get(`/study/${user_id}/${problem_id}/`);
};

const getRecentProblem = async (user_id) => {
  return await instance.get(`/study/recent/${user_id}/`);
};

const saveCodeInDB = async (problem, user, user_code, code_idx) => {
  return await instance.post(`/study/save/`, {
    problem,
    user,
    user_code,
    code_idx,
  });
};

const executeCode = async (user_code) => {
  return await instance.post(`/study/run/`, {
    user_code,
  });
};

const gradeCode = async (user_code, problem_id) => {
  return await instance.post(`/study/grade/`, {
    user_code,
    problem_id,
  });
};

const submitCode = async (problem, user, user_code, code_idx) => {
  return await instance.post(`/study/submit/`, {
    problem,
    user,
    user_code,
    code_idx,
  });
};

const runTestcase = async (user_code, input, output) => {
  return await instance.post(`/study/testcase/`, {
    user_code,
    input,
    output,
  });
};

export {
  getLecture,
  getAssignment,
  getProblems,
  getProblem,
  getProblemDetail,
  getRecentProblem,
  saveCodeInDB,
  executeCode,
  gradeCode,
  submitCode,
  runTestcase,
};
