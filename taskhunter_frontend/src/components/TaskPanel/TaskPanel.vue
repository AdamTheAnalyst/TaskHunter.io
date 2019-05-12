<template>
  <div class="col-md-12 task-panel">
      <ul>
        <transition-group name="list" enter-active-class="animated fadeIn" leave-active-class="animated fadeOut">
          <li v-for="task in tasks" :key='task.id'>
            <div class="task-row">
                <div class="row">
                  <div class="col-md-2 col-sm-4 col-4 task-due" v-on:click="showTask(task.id)">
                    <button v-bind:class="taskWarnings(task)" class="btn-sm badge-due">
                        <span v-if="shownTasks.includes(task.id)"> {{task.due_date | formatDateCalendar}}
                        </span>
                        <span v-else> 
                        {{task.due_date | formatDateDue}}
                        </span>
                    </button>
                  </div>
                  <div class="col-md-8 col-sm-6 col-6 task-title" v-on:click="showTask(task.id)">
                    {{ task.title }}
                  </div>
                  <div class="col-md-2 col-sm-2 col-2 task-buttons">
                    <button class="btn-sm btn-success buttons-task" v-on:click="markAsDone(task)"><span class="button-text">Done</span><i class="fas fas-white fa-check-square"></i></button>
                  </div>
                </div>
            </div>
          </li>
        </transition-group>
      </ul>
  </div>
</template>

<!--Componant Logic-->
<script>
import { mapState } from 'vuex';
export default {
  name: 'dashboard',
  data() {
    return {
      shownTasks: [],
      tasks: []
    }
  },
  components: {},
  mounted() {
    this.refreshTasks();
    this.timer = setInterval(this.refreshTasks, 1000)
  },
  computed: {
    ...mapState([
      'loggingIn',
      'loginError',
      'loginSuccessful',
      'accessToken'
    ])
  },
  methods: {
    showTask(reference){
      if (this.shownTasks.includes(reference)){
        this.shownTasks.pop(reference)
      }else{
        this.shownTasks.push(reference)
      }
    },
    taskWarnings(task){
      var now = new Date();
      var due_date = new Date(task.due_date);
      if (due_date > now){
        return {
          'btn-success':true,
          'btn-sm': true,
          'badge-due': true
        }
      }else{
        return {
          'btn-danger':true,
          'btn-sm': true,
          'badge-due': true
        }
      }
    },
    refreshTasks() {
      if (this.accessToken && this.loginSuccessful){
        this.axios.get(this.api_config.API_LOCATION+"/tasks/")
          .then(response => {this.tasks = response.data})
          .catch(error => {
              console.log(error);
          });
      }else{
        clearInterval(this.timer)
      }
    },
    remove(id){
      this.axios.delete(this.api_config.API_LOCATION+"/tasks/"+this.tasks[id].id+"/");
      this.tasks.splice(id, 1);
      this.refreshTasks();
    },
    cancelAutoUpdate(){
      clearInterval(this.timer) 
    },
    beforeDestroy() {
      clearInterval(this.timer)
    },
    markAsDone(task) {
      var now = new Date();
      task.completed_date = now.toISOString();
      this.axios.put(this.api_config.API_LOCATION+"/tasks/"+task.id+"/", task)
      this.refreshTasks();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./TaskPanel.css" scoped></style>
