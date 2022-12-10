import { React, useRef } from "react";
import { DiffEditor } from "@monaco-editor/react";

const CodeDiff = (props) => {
  const editorRef = useRef(null);

  const handleEditorDidMount = (editor, monaco) => {
    editorRef.current = editor;
  };

  return (
    <DiffEditor
      theme="vs-dark"
      height="100%"
      language="python"
      original={props.code}
      modified={props.solutionCode}
      onMount={handleEditorDidMount}
      options={{ readOnly: true, renderSideBySide: props.expanded }}
    />
  );
};

export default CodeDiff;
