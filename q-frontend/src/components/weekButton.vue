<template>
  <q-item clickable v-ripple :to="'/' + this.$route.params.year + '/' + this.week.number"
    :class="'text-white ' + (this.$route.params.week == this.week.number ? 'bg-info' : '')">
    <q-item-section>
      <q-item-label class="text-h6">{{ this.fromDate }}</q-item-label>
      <q-item-label class="text-h6">{{ this.toDate }}</q-item-label>
    </q-item-section>
    <q-item-section avatar>
      <q-avatar size='64px' color="" text-color="white">
        {{ week.number }}
      </q-avatar>
    </q-item-section>
  </q-item>
</template>

<script>
export default {
  name: 'WeekButton',
  props: ['week'],
  setup() {
    return {}
  },
  data() {
    return {
      fromDate: null,
      toDate: null,
    }
  },
  mounted() {
    const from = this.week.from
    const to = this.week.to
    this.fromDate = `${from.day}.${from.month}.${from.year}`
    this.toDate = `${to.day}.${to.month}.${to.year}`
  }
}
</script>
