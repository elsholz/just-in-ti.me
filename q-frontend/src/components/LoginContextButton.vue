<template>
  <q-btn v-if="isAuthenticated" :label="user.nickname" color="green-5" outline
    class="q-pa-sm q-px-md q-mx-lg text-body1" icon="person" />
  <q-btn v-else @click="login" v-label="Login" color="green-6" :label="$q.platform.is.mobile ? '' : 'Login'"
    class="q-pa-sm q-px-md q-mx-lg text-body1" icon="person" />
</template>

<script>
import { useAuth0 } from '@auth0/auth0-vue'
import { useQuasar } from 'quasar'

export default {
  mounted() {
    const { checkSession } = useAuth0()
    checkSession()
  },
  setup() {
    const $q = useQuasar()
    const { loginWithRedirect } = useAuth0();
    return {
      login: async () => {
        loginWithRedirect()
      },
    }
  },
  data() {
    const { user, isAuthenticated } = useAuth0();
    return {
      user,
      isAuthenticated,
    }
  }
}
</script>
