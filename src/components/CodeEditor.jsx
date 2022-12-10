import { React, useEffect, useRef } from "react";
import Editor from "@monaco-editor/react";

const CodeEditor = (props) => {
  const editorRef = useRef(null);

  useEffect(() => {
    if (editorRef.current !== null) {
      props.setCode(editorRef.current.getValue());
    }
  }, [editorRef.current]);

  const handleEditorDidMount = (editor, monaco) => {
    editorRef.current = editor;
  };

  const handleEditorChange = (editor) => {
    props.setCode(editorRef.current.getValue());
  };

  return (
    <Editor
      theme="vs-dark"
      height="100%"
      defaultLanguage="python"
      value={props.code}
      onMount={handleEditorDidMount}
      onChange={handleEditorChange}
    />
  );
};

export default CodeEditor;
