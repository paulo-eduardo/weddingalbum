<template>
    <div>
        <a href="#!" class="collection-item">
            <img :src="pictureURI" height="20px" width="auto" />
            <span class="badge">{{status}}</span>
            {{picture.name}}
        </a>
    </div>
</template>

<script>
export default {
  props: ['picture'],
  data( ) {
    return {
        pictureURI: '',
        status: 'Uploading',
    }
  },
  mounted () {
    var image = new Image();
    var reader = new FileReader();
    var vm = this;

    reader.onload = (e) => {
    vm.pictureURI = e.target.result;
    };
    
    reader.readAsDataURL(this.picture);
    var data = new FormData();
    data.append('img', this.picture)
    const init = { 
        method: 'POST',
        body: data
    };
    fetch(localStorage.link +"/pictures/", init)
    .then((response) => {
        if(response.status == 201){
            this.status = "Uploaded";
        } else {
            this.status = "Error"
        }
    })
  },
  methods: {
      createImage(file) {
      var image = new Image();
      var reader = new FileReader();
      var vm = this;
      
      reader.onload = (e) => {
        return e.target.result;
      };
      
      reader.readAsDataURL(file);
    },
  }
}
</script>

<style>
.box {
    width:50%;
    margin-left:25%; /* half of width */
    margin-top:25%px;  /* half of height */
    top:50%;
    left:50%;
}
</style>
