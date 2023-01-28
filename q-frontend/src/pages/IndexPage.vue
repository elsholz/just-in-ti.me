<template>
  <q-page>
    <!--<img alt="Quasar logo" src="~assets/quasar-logo-vertical.svg" style="width: 200px; height: 200px">
    {{ this.getDate() }} <br>
    Info: {{ info }} <br>
    Parsed: {{ parsed }}-->

    <div class="row text-white bg-secondary">
      <div class="col-3" style="border-right: 2px solid #fff7; overflow: auto; max-height: 80vh;">
        <q-page style="overflow-y: auto;">
          <WeekList></WeekList>
        </q-page>
      </div>
      <div class="col text-white bg-secondary" style="overflow-y: hidden;">
        <q-page>
          <WeekView></WeekView>
        </q-page>
      </div>
    </div>
  </q-page>
</template>


<script>
import axios from 'axios'
import WeekList from 'src/components/weekList.vue';
import WeekView from 'src/components/weekView.vue';
import { defineComponent } from 'vue'

export default defineComponent({
  name: "IndexPage",
  data: function () {
    return {
      info: undefined,
      parsed: undefined,
    };
  },
  mounted: function () {
    /*
    axios.get("/api/_userdata").then(response => {
      this.info = response.data;
      for (const [y, months] of Object.entries(this.info.hours)) {
        for (const [m, days] of Object.entries(months)) {
          for (const [d, timeSlots] of Object.entries(days)) {
            const date = new Date(y, m - 1, d);
            console.log(date);
            this.parsed = date;
          }
        }
      }
    });*/
  },
  components: { WeekList, WeekView }
})
</script>
