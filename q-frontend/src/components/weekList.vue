<template>
  <q-list dark separator style="overflow-y: scroll">
    <WeekButton v-for="w in this.weeks" v-bind:key="w" :week="w"></WeekButton>
  </q-list>
</template>

<script>
import WeekButton from './weekButton.vue';
import moment from 'moment';

export default {
  data() {
    return {
      weeks: [],
      year: undefined
    }
  },
  setup() {
    return {};
  },
  watch: {
    '$route.params.year': {
      handler: function (year) {
        // nothing changed in this case.
        if (this.year === year)
          return

        this.year = year
        let mom = moment(year)
        mom.add(-mom.isoWeekday() + 1, 'day')
        const lastDayOfYear = moment(year).add(1, 'year').add(-1, 'day')
        const numWeeks = 52 + (lastDayOfYear.isoWeek() === 1 ? 1 : 0)

        let res = []

        for (let i = 0; i <= numWeeks; i++) {
          const start = mom.clone()

          mom.add(1, 'isoWeek')

          let end = mom.clone()
          end.add(-1, 'day')

          const obj = {
            number: i + 1,
            from: {
              year: start.year().toString(),
              month: (start.month() + 1).toString().padStart(2, '0'),
              day: start.date().toString().padStart(2, '0'),
            },
            to: {
              year: end.year(),
              month: (end.month() + 1).toString().padStart(2, '0'),
              day: end.date().toString().padStart(2, '0'),
            }
          }
          res.push(obj)
        }
        this.weeks = res
      },
      deep: true,
      immediate: true
    }
  },

  components: { WeekButton }
}
</script>
