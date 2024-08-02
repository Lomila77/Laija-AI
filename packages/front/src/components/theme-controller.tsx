import exp from "constants";
import React from "react";

const ThemeController: React.FC = () => {
    return (
        <label className="cursor-pointer grid place-items-center bg-neutral">
            <input type="checkbox" value="synthwave" className="toggle theme-controller bg-accent hover:bg-accent row-start-1 col-start-1 col-span-2"/>
            <svg className="col-start-1 row-start-1 stroke-neutral fill-neutral" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="fill-neutral" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>
            <svg className="col-start-2 row-start-1 stroke-neutral fill-neutral" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="fill-neutral" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
        </label>
    )
}

export default ThemeController;
