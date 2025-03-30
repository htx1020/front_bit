import React, { useState } from 'react';
import { API_BASE_URL } from '../config';

const InputDisplayComponent = () => {
    // 使用 useState 钩子来管理输入框的值和显示框的内容
    const [inputValue, setInputValue] = useState('');
    const [displayText, setDisplayText] = useState('');

    // 处理提交按钮的点击事件
    const handleSubmit = async () => {
        try {
            const response = await fetch(`${API_BASE_URL}/items/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: inputValue })
            });
            if (response.ok) {
                const data = await response.json();
                setDisplayText(JSON.stringify(data));
            } else {
                console.error('请求失败:', response.status);
            }
        } catch (error) {
            console.error('发生错误:', error);
        }
        setInputValue('');
    };
    return (
        <div>
            {/* 输入框 */}
            <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                placeholder="请输入内容"
            />
            {/* 提交按钮 */}
            <button onClick={handleSubmit}>提交</button>
            {/* 显示框 */}
            <div>{displayText}</div>
        </div>
    );
};

export default InputDisplayComponent;