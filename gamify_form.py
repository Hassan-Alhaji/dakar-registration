import re

def gamify_form(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS for temp gauge and custom switches
    css_to_add = """
    /* Rally Switches */
    .form-switch .form-check-input {
        width: 4rem;
        height: 2rem;
        background-color: #333;
        border: 2px solid #555;
        border-radius: 20px;
        transition: all 0.3s;
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.8);
        cursor: pointer;
    }
    .form-switch .form-check-input:checked {
        background-color: var(--neon-green);
        border-color: var(--neon-green);
        box-shadow: 0 0 15px var(--neon-green);
    }
    .form-switch .form-check-input::after {
        background-color: #fff;
        border-radius: 50%;
        box-shadow: 0 2px 5px rgba(0,0,0,0.5);
    }

    /* Temp Gauge */
    .temp-gauge-container {
        display: flex;
        gap: 10px;
        margin-top: 10px;
    }
    .temp-segment {
        flex: 1;
        height: 40px;
        background: #222;
        border: 2px solid #444;
        cursor: pointer;
        transition: all 0.3s;
        transform: skewX(-15deg);
        position: relative;
    }
    .temp-segment::after {
        content: attr(data-val);
        position: absolute;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%) skewX(15deg);
        color: #fff;
        font-weight: 800;
        opacity: 0.5;
    }
    .temp-segment:hover { opacity: 0.8; }
    .temp-segment.active-1 { background: #00f3ff; border-color: #00f3ff; box-shadow: 0 0 10px #00f3ff; }
    .temp-segment.active-1::after { opacity: 1; color: #000; }
    .temp-segment.active-2 { background: #00ff41; border-color: #00ff41; box-shadow: 0 0 10px #00ff41; }
    .temp-segment.active-2::after { opacity: 1; color: #000; }
    .temp-segment.active-3 { background: #ffe600; border-color: #ffe600; box-shadow: 0 0 10px #ffe600; }
    .temp-segment.active-3::after { opacity: 1; color: #000; }
    .temp-segment.active-4 { background: #ff7b00; border-color: #ff7b00; box-shadow: 0 0 10px #ff7b00; }
    .temp-segment.active-4::after { opacity: 1; color: #000; }
    .temp-segment.active-5 { background: #ff003c; border-color: #ff003c; box-shadow: 0 0 10px #ff003c; }
    .temp-segment.active-5::after { opacity: 1; color: #fff; }

    /* RPM Bar */
    #rpm-progress-container {
        position: fixed;
        bottom: 0; left: 0; right: 0;
        background: rgba(11, 12, 16, 0.95);
        border-top: 2px solid var(--neon-green);
        z-index: 1000;
        padding: 15px 0;
        transform: translateY(100%);
        transition: transform 0.5s ease;
    }
    #rpm-progress-container.show {
        transform: translateY(0);
    }
    #car-indicator {
        transition: left 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    }
"""

    if "/* Rally Switches */" not in content:
        content = content.replace('</style>', css_to_add + '\n</style>')

    # 2. Add RPM Bar HTML just before </form>
    rpm_html = """
                    <!-- Submit -->
                    <div class="text-start mt-5 pt-4 border-top border-secondary gs-reveal pb-5 mb-5">
                        <button type="submit" id="submitBtn" class="btn btn-neon btn-lg w-100 py-3">
                            <i class="fas fa-bolt me-2"></i> {% trans "إرسال طلب التسجيل" %}
                        </button>
                    </div>
                </form>

                <!-- RPM Progress Bar -->
                <div id="rpm-progress-container">
                    <div class="container d-flex align-items-center position-relative">
                        <i class="fas fa-flag-checkered fs-4 text-white me-3"></i>
                        <div class="progress w-100" style="height: 25px; background: #222; border-radius: 12px; overflow: visible; position: relative;">
                            <div id="rpm-bar" class="progress-bar progress-bar-striped progress-bar-animated bg-success" role="progressbar" style="width: 0%; border-radius: 12px; transition: width 0.4s ease, background-color 0.4s ease;" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            <i class="fas fa-car-side fs-3 position-absolute" id="car-indicator" style="color: var(--white); top: -20px; left: 0%; filter: drop-shadow(0 0 5px var(--white));"></i>
                        </div>
                        <span id="rpm-text" class="ms-3 fw-bold text-neon" style="min-width: 50px;">0%</span>
                    </div>
                </div>
"""
    # Replace the existing submit block
    submit_pattern = r'<!-- Submit -->.*?</div>\s*</form>'
    content = re.sub(submit_pattern, rpm_html, content, flags=re.DOTALL)

    # 3. Add JS
    js_to_add = """
        // Temp Gauge Logic
        const ratingInput = document.getElementById('id_desert_driving_rating');
        if (ratingInput) {
            ratingInput.style.display = 'none';
            const gaugeHTML = `
                <div class="temp-gauge-container">
                    <div class="temp-segment" data-val="1"></div>
                    <div class="temp-segment" data-val="2"></div>
                    <div class="temp-segment" data-val="3"></div>
                    <div class="temp-segment" data-val="4"></div>
                    <div class="temp-segment" data-val="5"></div>
                </div>
            `;
            ratingInput.insertAdjacentHTML('afterend', gaugeHTML);
            
            const segments = document.querySelectorAll('.temp-segment');
            segments.forEach(seg => {
                seg.addEventListener('click', function() {
                    const val = parseInt(this.getAttribute('data-val'));
                    ratingInput.value = val;
                    // Update visuals
                    segments.forEach(s => {
                        const sVal = parseInt(s.getAttribute('data-val'));
                        s.className = 'temp-segment'; // reset
                        if (sVal <= val) {
                            s.classList.add('active-' + sVal);
                        }
                    });
                });
            });
            // Init if value exists
            if(ratingInput.value) {
                document.querySelector(`.temp-segment[data-val="${ratingInput.value}"]`).click();
            }
        }

        // RPM Progress Bar Logic
        const form = document.getElementById('registrationForm');
        const requiredInputs = form.querySelectorAll('input[required], select[required], textarea[required]');
        const rpmContainer = document.getElementById('rpm-progress-container');
        const rpmBar = document.getElementById('rpm-bar');
        const rpmText = document.getElementById('rpm-text');
        const carIndicator = document.getElementById('car-indicator');

        function updateProgress() {
            let filled = 0;
            requiredInputs.forEach(input => {
                if (input.type === 'checkbox' || input.type === 'radio') {
                    if (input.checked) filled++;
                } else if (input.value.trim() !== '') {
                    filled++;
                }
            });
            
            const total = requiredInputs.length || 1; // avoid div by 0
            let percentage = Math.round((filled / total) * 100);
            
            if (percentage > 0) {
                rpmContainer.classList.add('show');
            }
            
            rpmBar.style.width = percentage + '%';
            carIndicator.style.left = `calc(${percentage}% - 15px)`;
            rpmText.innerText = percentage + '%';
            
            // Color mapping based on RPM concept
            rpmBar.className = 'progress-bar progress-bar-striped progress-bar-animated';
            if (percentage < 33) {
                rpmBar.classList.add('bg-success');
                carIndicator.style.color = '#00ff41';
            } else if (percentage < 66) {
                rpmBar.classList.add('bg-warning');
                carIndicator.style.color = '#ffe600';
            } else if (percentage < 100) {
                rpmBar.classList.add('bg-danger');
                carIndicator.style.color = '#ff003c';
            } else {
                rpmBar.style.backgroundColor = '#00f3ff';
                rpmBar.classList.remove('bg-success', 'bg-warning', 'bg-danger');
                carIndicator.style.color = '#00f3ff';
            }
        }

        // Add event listeners to all inputs
        form.querySelectorAll('input, select, textarea').forEach(input => {
            input.addEventListener('input', updateProgress);
            input.addEventListener('change', updateProgress);
        });

        // Launch animation on submit
        form.addEventListener('submit', function(e) {
            if (form.checkValidity()) {
                // Animate car zooming off
                gsap.to(carIndicator, {left: '120%', duration: 1.5, ease: "power2.in"});
                gsap.to(rpmContainer, {opacity: 0, duration: 1, delay: 0.5});
            }
        });
        
        updateProgress(); // Initial check
"""

    if "// Temp Gauge Logic" not in content:
        content = content.replace('// Form reveals', js_to_add + '\n        // Form reveals')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

gamify_form('templates/registration_form.html')
print('Form Gamified!')
