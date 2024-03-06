import { useLocation, Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { selecCurrentToken } from "../../store/authSlice";

const RequireAuth = () =>{
    const token = useSelector(selecCurrentToken);
    const location = useLocation();
    if(token){
        return {message: "Okay"}
    }
    else{
        return <Navigate to="/login" state={{from:location}} replace/>
    }
}

export default RequireAuth;