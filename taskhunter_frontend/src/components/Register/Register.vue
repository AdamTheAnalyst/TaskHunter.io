<template>
  <div class="col-md-4 offset-md-4 col-sm-12 col-12">
    <div class="register-panel">
      Register with TaskHunter<br>
    <span v-if="form_error" class="badge badge-danger">
      {{form_error}}
    </span>
    <router-link to="/login">
      <span v-if="form_success" class="badge badge-success">
        Success! Click here to login.
      </span>
    </router-link>
      <form v-on:submit.prevent autocomplete="off">
      <table class="register-table" autocomplete="off">
        <tr>
          <td class="register-value">
            <input v-model="first_name" autocomplete="false" placeholder="First name" class="form-control register-form-input">
          </td>
        </tr>
        <tr>
          <td class="register-value">
            <input v-model="last_name" autocomplete="false" placeholder="Last name" class="form-control register-form-input">
          </td>
        </tr>
        <tr>
          <td class="register-value">
            <input v-model="email" autocomplete="new-email" placeholder="Email" class="form-control register-form-input">
          </td>
        </tr>
        <tr>
          <td class="register-value">
            <input v-model="password" autocomplete="new-password" type="password" placeholder="Password" class="form-control register-form-input">
          </td>
        </tr>
        <tr>
          <td class="register-value">
            <button class="btn-sm btn-success register-buttons" v-on:click="register()">Submit</button>
          </td>
        </tr>
      </table> 
      </form>
    </div>
  </div>
</template>
<!--Componant Logic-->
<script>

export default {
  name: 'register',
  data() {
    return {
      form_error: null,
      form_success: false,
      first_name: null,
      last_name: null,
      email: null,
      password: null,
    }
  },
  methods: {
    register() {
      this.form_success = false;
      this.form_error = null;
      var user = {
        first_name: this.first_name,
        last_name: this.last_name,
        email: this.email,
        password: this.password,
      }
      this.axios.post(this.api_config.API_LOCATION+"/users/", user)
      .then(response => {
        this.form_success = response;
      })
      .catch(error => {
        this.form_error = error.response.data
      });
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./Register.css" scoped></style>
