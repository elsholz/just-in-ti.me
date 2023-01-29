<template>
  <q-layout view="hHh lpR fff">

    <q-header class="bg-primary text-white">
      <q-toolbar>
        <q-btn round flat padding="md" size="lg" icon="today" href="https://github.com/elsholz/just-in-ti.me/"></q-btn>
        <q-btn round flat padding="md" size="lg" icon="fa-brands fa-github"
          href="https://github.com/elsholz/just-in-ti.me/"></q-btn>

        <q-toolbar-title class="text-center">
          <q-btn no-caps flat padding="md" class="text-h4" to="/">
            <span class="text-bold">
              just-in-ti
            </span>
            <span class="text-bold text-grey-5">
              .me
            </span>
          </q-btn>
        </q-toolbar-title>
        <q-btn padding="md" no-caps flat to="/impressum">
          Impressum
        </q-btn>
        <q-btn padding="md" no-caps flat to="/privacy">
          Privacy
        </q-btn>
        <LoginContextButton></LoginContextButton>

      </q-toolbar>
      <q-tabs align="left">
        <q-route-tab v-for="y in this.years" :key="y" class="q-pa-none q-px-xl"
          :to="'/' + y + '/' + ((this.$route.params.year === y) ? this.$route.params.week : '1')" :label="y" />
      </q-tabs>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>

  </q-layout>
</template>

<style>
.q-tab__label {
  font-size: 2em;
  font-weight: bold;
}
</style>

<script>
import LoginContextButton from 'src/components/LoginContextButton.vue'
import { defineComponent, ref } from 'vue'
import moment from 'moment'
import { useAuth0 } from '@auth0/auth0-vue'
import axios from 'axios'

export default defineComponent({
  name: 'MainLayout',
  data: function () {
    return {
      userData: null,
      years: [],
    }
  },
  mounted: async function () {
    const { getAccessTokenSilently } = useAuth0();
    const token = await getAccessTokenSilently();

    axios.get('/api/_userdata', {
      headers: {
        authorization: 'Bearer ' + token
      }
    }).then(response => {
      this.userData = response.data
      this.years = Object.keys(this.userData.hours)
      // const now = new Date()
      const selectedYear = this.$route.params.year
      console.log(selectedYear)

      if (!this.years.includes(selectedYear)) {
        this.years.push(selectedYear)
      }

      this.years.sort()
    })
  },
  setup() {
    return {
    }
  },
  components: { LoginContextButton }
})
</script>
