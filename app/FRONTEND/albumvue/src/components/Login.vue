<template>
  <div class="login">
        <h5> To have access to this page you have to login </h5>
        <span v-if="this.error" class="helper-text" data-error="wrong" data-success="right"> {{this.error}} </span>        
        <div class="input-field col s12">
          <input id="login" type="text" class="validate" placeholder="Login" v-model="login.username">
        </div>
        <div class="input-field col s12">
          <input id="password" type="password" placeholder="Password" class="validate" v-model="login.password">
        </div>
        <button v-if="this" v-on:click="obtainToken(login.username, login.password)" class="btn"> Login </button> 
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Login',
    props: {
        msg: String
    },
    data() {
        return {
            login: {
                username: "",
                password: "",
            },
            error: null 
        }
    },
    methods: {
        obtainToken(user, password){
        const payload = {
            username: user,
            password: password
        }
        axios.post(localStorage.link +'/api-token-auth/', payload)
            .then((response)=>{
                localStorage.token = response.data['token'];
                this.$router.push('/Approving')
            })
            .catch((error)=>{
                this.error = "Login ou senha incorretos";
            })
        },
    }
}
</script>

<style>
.login { 
  width: 400px;
  margin: auto;
  margin-top: 100px;
}

.helper-text {
    color: red;
}
</style>
