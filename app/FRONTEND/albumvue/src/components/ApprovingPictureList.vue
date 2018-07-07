<template>
    <div class='row'>
        <div v-if="pictures.length == 0">
            <h3>No pictures to display </h3>
        </div>
        <div  v-else>
            <div class="col m3" v-for="picture in pictures" :key="picture.id" v-if="picture.status === null">
                <ApprovingPicture v-bind:picture="picture"/>
            </div>
        </div>
    </div>
</template>


<script>
import ApprovingPicture from './ApprovingPicture.vue'

export default {
    components: {
        'ApprovingPicture': ApprovingPicture
    },
    data () {
        return {
            pictures: null
        }
    },
    mounted() {
        fetch(localStorage.link +'/pictures/toApprove/', {
             headers: {
                 Authorization: "JWT " + localStorage.token
             },
            method: 'GET'
        }).then(response => response.json())
        .then(data => {
            if(data.detail){
                this.$router.push('/Login')
            }
            this.pictures = data;
        })
    }
}
</script>
