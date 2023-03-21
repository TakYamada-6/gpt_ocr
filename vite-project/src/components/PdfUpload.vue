<template>
  <div id="pdf_upload">
    <h1>ビズリーチ経歴要約</h1>
    <p>PDFファイルをアップロードしてください。PDFはユーザーのプロフィールを開き、下までスクロールしてブラウザの印刷から最後まで収まるようにA1～A3でPDFに保存してください。</p>
    <input type="file" @change="uploadPdf" />
    <p v-if="userName">user_name: {{ userName }}</p>
    <p v-if="summarizeResume">summarize_resume: {{ summarizeResume }}</p>
    <p v-if="error" class="error">{{ error }}</p>

  </div>
</template>

<script>
export default {
  name: "pdf_upload",
  data() {
    return {
      summarizeResume: "",
      error: "",
    };
  },
  methods: {
    async uploadPdf(event) {
      console.log("Uploading PDF...");

      const file = event.target.files[0];
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://localhost:8000/api/upload_pdf", {
          method: "POST",
          body: formData,
        });
        const data = await response.json();

        console.log("API Response:", data);

        if (data.error) {
          this.error = data.error;
          console.error(data.error);
        } else {
          this.userName = data.user_name;
          this.summarizeResume = data.summarize_resume;
        }
      } catch (error) {
        console.error("Error while uploading PDF:", error);
      }
    }
  },
};
</script>
