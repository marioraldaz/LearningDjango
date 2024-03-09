import { useLocation, Navigate } from "react-router-dom";
import { useSelector } from "react-redux";
import { selectCurrentToken } from "../../redux/authSlice";

export const RequireAuth = () =>{
    const token = useSelector(selectCurrentToken);
    const location = useLocation();
    if(token){
        return {message: "Okay"}
    }
    else{
        return <Navigate to="/login" state={{from:location}} replace/>
    }
}

