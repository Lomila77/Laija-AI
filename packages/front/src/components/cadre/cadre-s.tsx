import React from "react";

interface CadreMProps {
    componentChildren: React.ReactNode;
}

const CadreS: React.FC<CadreMProps> = ({ componentChildren }) => {
    return (
        <div className="flex flex-col items-center justify-center bg-neutral size-16 rounded-full inner-shadow-neutral box-border border-4 border-accent">
            {componentChildren}
        </div>
    )
}

export default CadreS;
