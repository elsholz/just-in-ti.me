<template>

  <div class="row text-center full-height q-pt-xl q-px-xl" style="background: #001">
    <div v-for="d in this.days" v-bind:key="d" class="col q-py-md">
      <q-page style="min-height: 73vh;">
        <div class="row q-pb-md">
          <div class="col">
            {{ d.weekday }}
          </div>
        </div>
        <div class="row" style="min-height: 60vh;">
          <div class="col"></div>
          <div class="col col-1" style="width: 2px; background-color: #ffc; min-height: inherit;">

          </div>
          <div class="col"></div>
        </div>
        <div class="row q-pt-md">
          <div class="col">
            {{ d.weekday }}
          </div>
        </div>
      </q-page>
    </div>
  </div>
</template>

<script>
export default {
  // name: 'ComponentName',
  setup() {
    return {}
  },
  data() {
    return {
      days: [
        {
          date: '2023-12-01',
          weekday: "Monday"
        },
        {
          date: '2023-12-01',
          weekday: "Tuesday"
        },
        {
          date: '2023-12-01',
          weekday: "Wednesday"
        },
        {
          date: '2023-12-01',
          weekday: "Thursday"
        },
        {
          date: '2023-12-01',
          weekday: "Friday"
        },
        {
          date: '2023-12-01',
          weekday: "Saturday"
        },
        {
          date: '2023-12-01',
          weekday: "Sunday"
        },
      ]
    }
  },
}
</script>
