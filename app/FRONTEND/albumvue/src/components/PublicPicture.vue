<template>
    <div class="card black z-depth-5">
        <div class="card-content white-text cardSize" align="center">
            <img class="picture" :src="picture.url"/>
        </div>
        <div class="card-action">
            <a v-on:click="like" class="btn-floating halfway-fab waves-effect waves-light blue-grey darken-4">
                <h3 v-if="liked" class="redHeart heart" align="center">&hearts;</h3>
                <h3 v-else class="whiteHeart heart" align="center">&hearts;</h3>
            </a>
            <a >Likes  {{picture.likes}}</a>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['picture'],
  data() {
      return {
          liked: false
      }
  },
  methods: {
      like() {
        if(!this.liked){
            this.liked = true
            this.picture.likes = this.picture.likes + 1;
            axios.put(localStorage.link +'/pictures/approved/',this.picture)
        } else {
            this.liked = false
            this.picture.likes = this.picture.likes - 1;
            axios.put(localStorage.link +'/pictures/approved/',this.picture)
        }
      }
  }
}
</script>

<style>
.cardSize {
    height: 300px;
}

.heart {
    align-items: center;
    margin-top: -5px;
}

.whiteHeart {
    color: white;
}

.redHeart {
    color: red;
}

</style>
