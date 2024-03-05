import axios from 'axios'

const UsersApi=axios.create({
    baseURL: "http://localhost:8000/user/api/v1/user/"
  })
export function getProfileByID(id){
   // const res = axios.get());
}

export function register(user){
  try{
    const { username, password, gender, date_of_birth,email } = user;
    return  UsersApi.post("/",{
      username: username,
      password: password,
      gender: gender,
      date_of_birth: date_of_birth,
      email
    });

  } catch (e) {
    console.log(e);
  }
}