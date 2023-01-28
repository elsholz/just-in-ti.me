<template>
  <q-page class="text-white bg-secondary text-center q-pa-md text-body1">
    <h4>
      Privacy
    </h4>
    <p>
      <i>Where is my data stored?</i> <br>
      Your data is stored in a database in the cloud within Europe and only accessible to you and the app admin.
      Your name is not directly attached the data your store in our app, it is stored under a pseudonym.
    </p>
    <p>
      <i>Are there any third-parties involved?</i> <br>
      Yes, we use a third-party service for user authentication, namely Auth0.
      This service stores the login information you provide on registration, like username or and email-address.
      As for the storage of the data, we use a service from Mongo DB.
      For hosting the application and related functions, we use AWS.
    </p>
    <p>
      <i>Is my data used commercially?</i> <br>
      No. You data is not and will never be used commercially by us, and that's a promise.
      We may however change the conditions to use the service, like adding a paid subscription or suspending the
      service, in the future.
    </p>
    <p>
      <i>What happens when I delete my account?</i> <br>
      When you decide to delete your account, we will delete all information you stored in our app.
    </p>
  </q-page>
</template>

<script>
export default {
  // name: 'ComponentName',
  setup() {
    return {}
  }
}
</script>
