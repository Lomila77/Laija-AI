import React from "react";

interface CadreMProps {
    componentChildren: React.ReactNode;
}

const CadreM: React.FC<CadreMProps> = ({ componentChildren }) => {
    return (
        <div className="flex flex-col items-center bg-neutral justify-center size-32 m-5 rounded-full inner-shadow-neutral box-border border-4 border-accent">
            {componentChildren}
        </div>
    )
}

export default CadreM;
