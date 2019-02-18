################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/ASF/common/boards/user_board/init.c 

OBJS += \
./src/ASF/common/boards/user_board/init.o 

C_DEPS += \
./src/ASF/common/boards/user_board/init.d 


# Each subdirectory must supply rules for building sources it contributes
src/ASF/common/boards/user_board/%.o: ../src/ASF/common/boards/user_board/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	arm-none-eabi-gcc -DNDEBUG -D__SAM4S4B__ -DBOARD=USER_BOARD -DARM_MATH_CM4=true -I"D:\eclipse\PanelDue\PanelDue\src\config" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\thirdparty\CMSIS\Lib\GCC" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\utils\cmsis\sam4s\include" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\common\utils" -I"D:\eclipse\PanelDue\PanelDue\src" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\utils\cmsis\sam4s\source\templates" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\utils" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\utils\preprocessor" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\common\boards" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\utils\header_files" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\common\boards\user_board" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\thirdparty\CMSIS\Include" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\pio" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\pmc" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\common\services\clock" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\common\services\delay" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\wdt" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\pwm" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\uart" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\matrix" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\efc" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\drivers\rstc" -I"D:\eclipse\PanelDue\PanelDue\src\ASF\sam\services\flash_efc" -Os -Wall -c -std=gnu99 -mthumb -MD -MP -mcpu=cortex-m3 -ffunction-sections -fdata-sections -nostdlib --param max-inline-insns-single=500 -mlong-calls -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


