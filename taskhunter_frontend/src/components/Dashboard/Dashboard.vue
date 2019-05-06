<template>
  <div>
    <v-task-create></v-task-create>
    <div class="row">
      <div class="col-sm-12 main-holder">
        <v-task-panel></v-task-panel>
      </div>
    </div>
  </div>
</template>

<!--Componant Logic-->
<script>

import TaskPanel from '../TaskPanel'
import TaskCreate from '../TaskCreate'

export default {
  name: 'Incidents',
  data() {
    return {}
  },
  components: {
    'v-task-panel': TaskPanel,
    'v-task-create': TaskCreate
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style src="./Dashboard.css" scoped></style>
