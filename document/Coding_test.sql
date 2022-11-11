CREATE TABLE problem(
  id INTEGER NOT NULL,
  description TEXT,
  created_date TEXT,
  restriction TEXT,
  reference TEXT,
  title TEXT,
  time_limit INTEGER,
  memory_limit INTEGER,
  lecture_id INTEGER NOT NULL,
  assignment_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT assignment_problem
    FOREIGN KEY (assignment_id) REFERENCES assignment (id),
  CONSTRAINT lecture_problem FOREIGN KEY (lecture_id) REFERENCES lecture (id)
);

CREATE TABLE code(
  id INTEGER NOT NULL,
  user_code TEXT,
  created_date TEXT,
  modified_date TEXT,
  type TEXT NOT NULL,
  idx INTEGER NOT NULL,
  problem_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT problem_code FOREIGN KEY (problem_id) REFERENCES problem (id),
  CONSTRAINT user_code FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE user(
  id INTEGER NOT NULL,
  email TEXT,
  password TEXT,
  role INTEGER,
  created_date TEXT,
  PRIMARY KEY(id)
);

CREATE TABLE testcase(
  id INTEGER NOT NULL,
  "isHidden" INTEGER NOT NULL,
  output TEXT,
  problem_id INTEGER NOT NULL,
  input INTEGER,
  idx INTEGER NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT problem_testcase FOREIGN KEY (problem_id) REFERENCES problem (id)
);

CREATE TABLE solution(
  id INTEGER NOT NULL,
  problem_id INTEGER NOT NULL,
  created_date TEXT,
  modified_date TEXT,
  answer_code TEXT NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT problem_solution FOREIGN KEY (problem_id) REFERENCES problem (id)
);

CREATE TABLE lecture(id INTEGER NOT NULL, title TEXT, PRIMARY KEY(id));

CREATE TABLE assignment(
  id INTEGER NOT NULL,
  lecture_id INTEGER NOT NULL,
  title TEXT,
  deadline TEXT,
  PRIMARY KEY(id),
  CONSTRAINT lecture_assignment FOREIGN KEY (lecture_id) REFERENCES lecture (id)
);

CREATE TABLE user_lecture(
  id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  lecture_id INTEGER NOT NULL,
  PRIMARY KEY(id),
  CONSTRAINT user_user_lecture FOREIGN KEY (user_id) REFERENCES user (id),
  CONSTRAINT lecture_user_lecture FOREIGN KEY (lecture_id) REFERENCES lecture (id)
);

CREATE TABLE submission(
  submission_id INTEGER NOT NULL,
  created_date INTEGER,
  submission_count INTEGER NOT NULL,
  problem_id INTEGER NOT NULL,
  user_id INTEGER NOT NULL,
  PRIMARY KEY(submission_id),
  CONSTRAINT problem_submission FOREIGN KEY (problem_id) REFERENCES problem (id),
  CONSTRAINT user_submission FOREIGN KEY (user_id) REFERENCES user (id)
);
