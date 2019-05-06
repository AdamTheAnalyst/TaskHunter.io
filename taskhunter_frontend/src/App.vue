<template>
   <div id="app">
      <header>
         <title>TaskHunter.io</title>
         <link rel="shortcut icon" type="image/png" href="/static/favicon.png"/>
      </header>
      <nav>
         <div class="top">
            <div class="logo">
               <router-link to="/"><h2 class="logo-text"><i class="fas fa-crosshairs"></i> TaskHunter.io</h2></router-link>
            </div>
            <div class="logged-in-user" v-show="username">
              <b-dropdown id="dropdown-1" text="Adam Bradbury" variant="success" size="sm" class="m-md-0">
                <template slot="button-content">
                  <span class="button-text">{{username}}</span> <i class="fas fas-white fa-user"></i>
                </template>
                <b-dropdown-item v-on:click="logout()">Log Out <i class="fas fas-black fa-sign-out-alt"></i></b-dropdown-item>
              </b-dropdown>      
            </div>
         </div>
      </nav>
      <body>
         <div class="main container-fluid">
            <router-view/>
         </div>
      </body>
   </div>
</template>

<script>
  import { mapActions, mapState } from 'vuex';
  export default {
    name: 'app',
    components: {
    },
    computed: {
      ...mapState([
        'loggingIn',
        'loginError',
        'loginSuccessful',
        'accessToken',
        'username'
      ])
    },
    methods:{
      ...mapActions([
        'fetchAccessToken',
        'doLogout'
      ]),
      logout(){
        this.doLogout();
        this.$router.push('/login')
      }
    },
    created() {
      this.fetchAccessToken();
      if (!this.accessToken && this.$route.path !== '/login' && this.$route.path !== '/register') {
        this.$router.push('/login?redirect=' + this.$route.path)
      }
    },
    updated () {
      this.fetchAccessToken();
      if (!this.accessToken && this.$route.path !== '/login' && this.$route.path !== '/register') {
        this.$router.push('/login?redirect=' + this.$route.path)
      }
    }
  }
</script>

<style src="./App.css"></style>
