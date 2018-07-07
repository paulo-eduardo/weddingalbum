<template>
    <div class='row'>
        <div v-if="pictures.length == 0">
            <h3>No pictures to display </h3>
        </div>
        <div  v-else>
            <div class="col m3" v-for="picture in pictures" :key="picture.id">
                <PublicPicture v-bind:picture="picture"/>
            </div>
        </div>
    </div>
</template>

<script>
import PublicPicture from './PublicPicture.vue'

export default {
    components: {
        'PublicPicture': PublicPicture
    },
    data () {
        return {
            pictures: null
        }
    },
    mounted() {
        fetch(localStorage.link +'/pictures/approved/', {
            method: 'GET'
        }).then(response => response.json())
        .then(data => {
            this.pictures = data;
            this.pictures.sort(function(a,b) {
                if(a.likes < b.likes) {
                    return 1;
                }
                if(a.likes > b.likes) {
                    return -1
                }
                return 0
            })
        })
    },
}
</script>