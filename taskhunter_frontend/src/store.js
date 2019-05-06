import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loggingIn: false,
    loginError: null,
    loginSuccessful: false,
    accessToken: null,
    username: null
  },
  mutations: {
    loginStart: state => state.loggingIn = true,
    loginStop: (state, errorMessage) => {
      state.loggingIn = false;
      state.loginError = errorMessage;
    },
    updateUsername: (state, userName) => {
      state.username = userName;
    },
    updateAccessToken: (state, accessToken) => {
      state.accessToken = accessToken;
      state.loginSuccessful = true;
    },
    logout: state => {
      state.loggingIn = false;
      state.loginError = null;
      state.accessToken = null;
      state.loginSuccessful = false;
    }
  },
  actions: {
    doLogin({ commit }, loginData) {
      commit('loginStart');

      axios.post(Vue.prototype.api_config.API_LOCATION+"/api-token-auth/", loginData)
      .then(response => {
        localStorage.setItem('accessToken', response.data.token);
        localStorage.setItem('userName', loginData.username);
        commit('loginStop', null);
        commit('updateAccessToken', response.data.token);
        commit('updateUsername', loginData.username);

        axios.interceptors.request.use(
          (config) => {
            let token = localStorage.getItem('accessToken');

            if (token) {
              config.headers['Authorization'] = `Token ${ token }`;
            }
            return config;
          }, 
          (error) => {
            return Promise.reject(error);
          }
        );
      })
      .catch(error => {
        commit('loginStop', error.response.data.non_field_errors[0]);
        commit('updateAccessToken', null);
        commit('updateUsername', null);
      });
    },
    doLogout({ commit }){
       console.log("State -> doLogout")
       localStorage.removeItem('accessToken');
       localStorage.removeItem('userName');
       commit('logout')
    },
    fetchAccessToken({ commit }) {
       console.log("State -> fetchAccessToken")
       commit('updateAccessToken', localStorage.getItem('accessToken'));
       commit('updateUsername', localStorage.getItem('userName'));
       axios.interceptors.request.use(
          (config) => {
            let token = localStorage.getItem('accessToken');

            if (token) {
              config.headers['Authorization'] = `Token ${ token }`;
            }
            return config;
          }, 
          (error) => {
            return Promise.reject(error);
          }
        );
    }
  }
})