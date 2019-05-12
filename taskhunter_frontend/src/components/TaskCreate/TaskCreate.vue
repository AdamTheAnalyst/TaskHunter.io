<template>
  <div class="row">
    <div class="col-md-12 title-form-column ">
      <form autocomplete="off" data-lpignore=true>
        <div class="input-group mb-3">
          <div class="input-group-prepend">
          <datetime v-model="task_due_date" type="datetime" data-lpignore=true :min-datetime="current_time" input-class="form-control" id="task_date_input" input-style="max-width:200px;text-align:center;background-color:#28a745;color:#FFFFFF;border:0px;border-top-right-radius: 0%;border-bottom-right-radius: 0%;cursor:pointer;"></datetime>
          </div>
          <input type="text" v-model="task_title" data-lpignore=true class="form-control" placeholder="Create a new task..." aria-label="Create a new task..." id="task_title_input">
          <div class="input-group-append">
            <button class="btn btn-success" v-on:click="createTask" type="button">
              <span class="button-text"> Create New Task</span> <i class="fas fas-white fa-plus-square"></i>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<!--Componant Logic-->
<script>

import { Datetime } from 'vue-datetime';

export default {
  name: 'taskcreate',
  data() {
    var now = new Date();
    now.setHours(now.getHours() + Math.round(now.getMinutes()/60));
    now.setMinutes(0);
    return {
      task_title: null,
      task_due_date: now.toISOString(),
      current_time: now.toISOString()
    }
  },
  components: {
    datetime: Datetime
  },
  methods: {
    createTask() {
      var task = {
        "title": this.task_title,
        "due_date": this.task_due_date,
      };
      this.axios.post(this.api_config.API_LOCATION+"/tasks/", task)
      this.$router.push('/');
      
      var now = new Date();
      now.setHours(now.getHours() + Math.round(now.getMinutes()/60));
      now.setMinutes(0);
      this.task_title = null;
      this.task_due_date = now.toISOString();
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./TaskCreate.css" scoped></style>
