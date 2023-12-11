import ctypes

def _get(obj, fname, i0=-1, i1=-1, i2=-1):
    try:
        if hasattr(obj, fname) == False:
            return None
        v_type = obj._types_[fname]
        if i2 != -1:
            assert i0 >= 0 and i1 >= 0
            o_attr = getattr(obj, fname)[i0][i1][i2]
        elif i1 != -1:
            assert i0 >= 0
            o_attr = getattr(obj, fname)[i0][i1]
        elif i0 != -1:
            o_attr = getattr(obj, fname)[i0]
        else:
            o_attr = getattr(obj, fname)
        v_type = obj._types_[fname]
        return _get_val_(v_type, o_attr)
    except Exception as e:
        return None
    
def _get_val_(value_type, values):
    global _ltype_
    try:
        if value_type == "B":
            if _ltype_ == "tcs" and len(bytes(values)) == 2:
                return int.from_bytes(bytes(values), byteorder="little", signed=False)
            return int.from_bytes(bytes(values), byteorder="big", signed=False)
        
        elif value_type == "D":
            return bytes(values).hex().upper()

        elif value_type == "C":
            cut_values = []  # 0x00 앞부분만 사용하도록 수정
            len_val = ctypes.sizeof(values)
            for i in range(0, len_val):
                if values[i] == 0x0:
                    break
                else:
                    cut_values.append(values[i])
            res = bytes(cut_values).decode("euc-kr", errors="ignore")
            res = res.replace("\x00", "").strip()
            return res
        elif value_type == "O":
            return values
        else:
            return None
    except Exception as e:
        return None
    
__all__ = [
    '_get_val_', '_get'
]
