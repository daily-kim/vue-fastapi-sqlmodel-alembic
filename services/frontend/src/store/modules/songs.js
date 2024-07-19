import axios from 'axios';

const state = {
  songs: null,
  song: null
};

const getters = {
  stateSongs: state => state.songs,
  stateSong: state => state.song,
};

const actions = {
  async createSong({dispatch}, song) {
    await axios.post('songs', song);
    await dispatch('getSongs');
  },
  async getSongs({commit}) {
    let {data} = await axios.get('songs');
    commit('setSongs', data);
  },
  async getSong({commit}, id) {
    let {data} = await axios.get(`song/${id}`);
    commit('setSong', data);
  },
  async patchSong(_, song) {
    await axios.patch(`song/${song.id}`, song);
  },
  async deleteSong(_, id) {
    await axios.delete(`song/${id}`);
  },
  clearSong(){
    return null;
  },
};

const mutations = {
  setSongs(state, songs){
    state.songs = songs;
  },
  setSong(state, song){
    state.song = song;
  },
  

};

export default {
  state,
  getters,
  actions,
  mutations
};