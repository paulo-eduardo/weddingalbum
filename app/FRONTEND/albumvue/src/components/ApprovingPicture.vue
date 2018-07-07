<template>
    <div class="card black z-depth-5">
        <div class="card-content white-text cardSize" align="center">
            <img class="picture" :src="picture.url">
        </div>
        <div class="card-action">
            <a v-on:click="approvePicture">Approve</a>
            <a v-on:click="removePicture">Remove</a>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['picture'],
  methods:{
      approvePicture() {
          this.picture['status'] = true;
          this.changePictureStatus();
      },
      removePicture() {
          this.picture['status'] = false;
          this.changePictureStatus();
      },
      changePictureStatus() {
        var config = {
            headers: {
                'Authorization': "JWT " + localStorage.token,
                'Content-type': 'application/json'
            },
        };

        axios.put(localStorage.link + '/pictures/toApprove/', this.picture, config)
        .catch(e => {
            this.$router.push('/Login')
        })
      }
  }
}
</script>

<style>
img.picture {
    height: auto;
    max-height: 280px;
    width: auto;
    max-width: 400px;
}

.cardSize {
    height: 300px;
}
</style>
