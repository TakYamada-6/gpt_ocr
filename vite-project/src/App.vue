<template>
  <div id="app" className="min-h-screen flex flex-col items-center justify-center">
    <div className="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
      <pdf-upload @file-uploaded="onFileUploaded"/>
      <summary-button :uploaded-file="uploadedFile"/>
    </div>
  </div>
</template>

<script>
import PdfUpload from "./components/PdfUpload.vue";
import SummaryButton from "./components/SummaryButton.vue";

export default {
  name: "App",
  components: {
    PdfUpload,
    SummaryButton,
  },
  data() {
    return {
      uploadedFile: null
    };
  },
  methods: {
    onFileUploaded(file) {
      console.log("Received file-uploaded event with file:", file);
      this.uploadedFile = file;
    }
  }
};
</script>
