const Avatar = ({ img }) => {
    return <div className="avatar avatar-placeholder inset-shadow-sm">
        <div className="w-12 rounded-full ring ring-accent ring-offset-accent ring-offset-2 inset-shadow-sm">
            <img src={img} />
        </div>
    </div>

}

export default Avatar;
