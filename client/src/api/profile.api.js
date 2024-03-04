import axios from 'axios'
export function getProfileByID(id){
    const res = axios.get(`http://localhost:800/profiles/api/v1/${id}`);
}