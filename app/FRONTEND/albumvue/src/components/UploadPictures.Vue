<template>
    <div>
      <div class="file-field input-field">
        <div class="btn black">
          <span>File</span>
          <input type="file" multiple v-on:change="onFileChange">
        </div>
        <div class="file-path-wrapper">
          <input class="file-path validate" type="text" placeholder="Upload one or more files">
        </div>
      </div>
      <div class="collection">
        <UploadedPicture v-for="picture in pictures" :key="picture.name" v-bind:picture="picture"/>
      </div>
    </div>
</template>

<script>
import UploadedPicture from './UploadedPicture.vue'

export default {
  data( ) {
    return {
      pictures: [],
      isPending: true
    }
  },
  methods: {
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length)
        return;
      var files_count = files.length;
      for(let i=0; i < files_count; i++){
        this.pictures.push(files[i]);
      }
    },
  },
  components: {
    'UploadedPicture': UploadedPicture
  },
}
</script>

