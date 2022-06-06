import React from 'react';

const Login = (props) => {
    return(
        <div className="spacer vm">
            <div className='container'>
             <div className='form-group col-md-6 mb-3'>
                 <label className='mb-2'>아이디(id)</label>
                 <input type="text" className='form-control' placeholder='아이디를 입력해주세요.'/>
              </div>
            <div className='form-group col-md-6 mb-3'>
                <label className='mb-2'>비밀번호</label>
                <input type="password" className='form-control' placeholder='비밀번호를 입력해주세요.'/>
            </div>
            <div className='form-group col-md-6 mb-3'>
                <label className='mb-2'>이름</label>
                <input type="text" className='form-control' placeholder='이름를 입력해주세요.'/>
            </div>
            <div className='form-group col-md-6 mb-3'>
                <label className='mb-2'>생일</label>
                <input type="date" className='form-control'/>
            </div>
            <div className='form-group col-md-6 mb-3'>
                <label className='mb-2'>닉네임</label>
                <input type="text" className='form-control' placeholder='닉네임을 입력해주세요.'/>
            </div>

        </div>
        </div>


    );

}

export default Login;