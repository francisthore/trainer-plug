import Assets from "../assets/Assets";
import {SolidButton, OutlineButton} from "./Button";


const Navbar = () => {
    const logo = Assets["logo_url"];

    return (
        <div className="flex justify-between items-center px-1 py-3 gap-1 bg-gray-50">
            <img src={ logo }
            alt="trainerplug logo"
            className="logo" 
            onClick={() => {window.location.href = "/"}}
            ></img>
            <div className="flex gap-2"> 
                <SolidButton onClick={() => {alert("yay you work")}}>
                    Become a Trainer
                </SolidButton>
                <OutlineButton onClick={() => {window.location.href = '/login'}}>
                    Login
                </OutlineButton>
            </div>
        </div>
    );
};

export default Navbar;
