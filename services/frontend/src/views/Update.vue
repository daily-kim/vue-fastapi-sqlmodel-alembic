<template>
  <section>
    <h1>UPDATE SONG</h1>
    <h2>1. Read song</h2>
    <div>
      <input type="text" v-model="id" placeholder="Enter Song ID" />
      <button @click="fetchSong()" class="btn btn-primary">getSong</button>
    </div>
    <div v-if="cur_song">
      Your Song name is <span style="color: red">{{ this.cur_song.name }}</span> and artist name is
      <span style="color: blue">{{ this.cur_song.artist }}</span
      >.
    </div>

    <h2>2. Update song</h2>
    <form @submit.prevent="updateSong">
      <div class="mb-3">
        <label for="name" class="form-label">Song Name:</label>
        <input type="text" name="name" v-model="updated_song.name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="artist" class="form-label">Artist Name</label>
        <input type="text" name="artist" v-model="updated_song.artist" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>

    <h2>3. Check updated</h2>
    <div>
      <button @click="fetchSong()" class="btn btn-primary">getSong</button>
    </div>
    <div v-if="cur_song">
      Your Song name is <span style="color: red">{{ this.cur_song.name }}</span> and artist name is
      <span style="color: blue">{{ this.cur_song.artist }}</span
      >.
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue'
import { mapGetters, mapActions } from 'vuex'
import _ from 'lodash'

export default defineComponent({
  name: 'update_song',
  data() {
    return {
      id: '',
      cur_song: null,
      updated_song: {
        id: '',
        name: '',
        artist: ''
      }
    }
  },
  computed: {
    ...mapGetters({ songs: 'stateSongs', song: 'stateSong' })
  },
  methods: {
    ...mapActions(['getSong', 'patchSong']),
    async fetchSong() {
      await this.getSong(this.id)
      this.cur_song = _.cloneDeep(this.song)
      this.updated_song = _.cloneDeep(this.song)
      console.log('Song fetched successfully')
      console.log(this.song)
    },
    async updateSong() {
      await this.patchSong(this.updated_song)
      console.log('Song updated successfully')
    }
  }
})
</script>
