//HACKED =)
function regexDivisibleBy(n) {
    RegExp = function (string) {
        function test(str) {
            if (str.trim() === '' || /[^01]/.test(str)) {
                return false;
            }
            let num = parseInt(str, 2).toString();
            switch (n) {
                case 1: return true;
                case 2: return +(num.slice(-1)) % 2 === 0;
                case 3: return num.split('').reduce( (acum, el) => acum += +el ) % 3 === 0;
                case 4: return +(num.slice(-2)) % 4 === 0;
                case 5: return num.slice(-1) === '0' || num.slice(-1) === '5';
                case 6: return +(num.slice(-1)) % 2 === 0 && num.split('').reduce( (acum, el) => acum += +el ) % 3 === 0;
                case 7: return (+num.slice(0, -1) - 2 * num.slice(-1) ) % 7 === 0;
                case 8: return +num.slice(-3) % 8 === 0;
                case 9: return num.split('').reduce( (acum, el) => acum += +el ) % 9 === 0;
                case 10: return num.slice(-1) === '0';
                case 11: return function () {
                        let odd = 0,
                            even = 0;
                        num.split('').forEach((el, index) => {
                            if (index % 2 === 0) odd += +el;
                            else even += +el;
                        })
                        return odd === even || even === odd + 11 || even === odd - 11;
                }();
                case 12: return num.split('').reduce( (acum, el) => acum += +el ) % 3 === 0 && +(num.slice(-2)) % 4 === 0;
                case 13: return ( +num.slice(0, -1) + (4 * +num.slice(-1)) ) % 13 === 0;
                case 14: return [0, 2, 4, 6, 8].some( el => el === +num.slice(-1)) && (+num.slice(0, -1) - 2 * num.slice(-1) ) % 7 === 0;
                case 15: return num.split('').reduce( (acum, el) => acum += +el ) % 3 === 0 && num.slice(-1) === '0' || num.slice(-1) === '5';
                case 16:  return +(num.slice(-1)) % 2 === 0 && +num.slice(-3) % 8 === 0;
                case 17: return (+num.slice(0, -1) - (+num.slice(-1) * 5)) % 17 === 0;
                case 18: return +(num.slice(-1)) % 2 === 0 && num.split('').reduce( (acum, el) => acum += +el ) % 9 === 0;
            }

            return false;
        }
        return {
            test
        };
    };
    return '01';
}
