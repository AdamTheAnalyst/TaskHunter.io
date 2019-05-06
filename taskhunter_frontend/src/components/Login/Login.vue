<template>
  <div class="col-md-4 offset-md-4 col-sm-12 col-12">
    <div class="login-panel">
      Welcome to TaskHunter,<br>
    <span v-if="loginError" class="badge badge-danger">
      {{loginError}}
    </span>
    <span v-if="loggingIn" class="badge badge-success"><!--Keep this here--></span>
      <form v-on:submit.prevent>
      <table class="login-table">
        <tr>
          <td class="login-value">
            <input v-model="username" autocomplete="current-username" placeholder="Username/Email" class="form-control login-form-input">
          </td>
        </tr>
        <tr>
          <td class="login-value">
            <input v-model="password" autocomplete="current-password" type="password" placeholder="Password" class="form-control login-form-input">
          </td>
        </tr>
        <tr>
          <td class="login-value">
            <button class="btn-sm btn-success login-buttons" v-on:click="createLogin()">Login</button>
            <router-link tag="button" class="btn-sm btn-success login-buttons" id="button" to="/register">Register</router-link>
          </td>
        </tr>
      
      </table> 
      </form>
    </div>
  </div>
</template>
<!--Componant Logic-->
<script>

import { mapState, mapActions } from 'vuex';
export default {
  name: 'login',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  computed: {
    ...mapState([
      'loggingIn',
      'loginError',
      'loginSuccessful',
      'accessToken'
    ])
  },
  created(){
    if (this.accessToken){
      this.$router.push(this.$route.params.redirect || '/');
    }
  },
  updated(){
    if (this.accessToken){
      this.$router.push(this.$route.params.redirect || '/');
    }
  },
  methods: {
    ...mapActions([
        'doLogin'
    ]),
    createLogin() {
      this.doLogin({
          username: this.username,
          password: this.password
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./Login.css" scoped></style>
